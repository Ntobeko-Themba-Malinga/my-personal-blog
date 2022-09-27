from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


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
    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'name': 'home'
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
    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'name': 'detail'
        }
    )


def about(request):
    return render(
        request,
        'blog/post/about.html',
        {
            'name': 'about'
        }
    )
