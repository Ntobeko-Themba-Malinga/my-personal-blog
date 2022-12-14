from queue import Empty
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.db.models import Count
from django.core.mail import send_mail

from taggit.models import Tag

from .models import Post, Project, About
from .forms import SubscriberForm, SearchForm


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    subscribe_form = SubscriberForm()
    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'name': 'home',
            'subscribe_form': subscribe_form
        }
    )


def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post_slug
    )
    subscribe_form = SubscriberForm()

    # similar posts
    post_tags = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags).exclude(id=post.id)
    similar_posts = similar_posts.annotate(
        num_tags=Count('tags')
    ).order_by('-num_tags', '-publish')[:4]

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'name': 'detail',
            'subscribe_form': subscribe_form,
            'similar_posts': similar_posts,
            'name': 'home'
        }
    )


def about(request):
    subscribe_form = SubscriberForm()
    about = About.objects.all().first()
    return render(
        request,
        'blog/post/about.html',
        {
            'name': 'about',
            'subscribe_form': subscribe_form,
            'about': about
        }
    )


@require_POST
def subscriber(request):
    form = SubscriberForm(request.POST)

    if form.is_valid():
        subscriber = form.save(commit=False)
        subscriber.save()

        subject = 'PythonTuts+ Subscription'
        message = f'Dear. {subscriber.email}\n\nThank you for subscribing to our newsletter\n\nRegards.\nPythonTuts+'

        send_mail(
            subject,
            message,
            'thembantobeko@gmail.com',
            [subscriber.email]
        )
        messages.success(
            request,
            "Successfully subscribed"
        )
    return redirect('blog:post_list')


@require_GET
def search(request):
    query = None
    form = SearchForm()
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.filter(
                title__contains=query
            )
    subscribe_form = SubscriberForm()
    return render(
        request,
        'blog/post/search.html',
        {
            'query': query,
            'results': results,
            'form': form,
            'subscribe_form': subscribe_form,
            'name': 'search'
        }
    )


def project_list(request):
    project_list = Project.published.all()
    paginator = Paginator(project_list, 6)
    page = request.GET.get('page')

    try:
        projects = paginator.page(page)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        projects = paginator.page(1)

    subscribe_form = SubscriberForm()
    return render(
        request,
        'blog/project/list.html',
        {
            'subscribe_form': subscribe_form,
            'projects': projects,
            'name': 'project'
        }
    )


def project_detail(request, project_slug):
    project = get_object_or_404(
        Project,
        status=Post.Status.PUBLISHED,
        slug=project_slug
    )
    subscribe_form = SubscriberForm()
    return render(
        request,
        'blog/project/detail.html',
        {
            'project': project,
            'subscribe_form': subscribe_form,
            'name': 'project'
        }
    )
