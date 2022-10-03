from django.urls import path
from .feeds import PostFeed
from . import views

app_name =  'blog'

urlpatterns = [
    # project list
    path(
        'projects/',
        views.project_list,
        name='project_list'
    ),
    # project detail
    path(
        'projects/<slug:project_slug>/',
        views.project_detail,
        name='project_detail'
    ),
    # search
    path(
        'search/',
        views.search,
        name='search'
    ),
    # subscribe
    path(
        'subscribe/',
        views.subscriber,
        name='subscribe'
    ),
    # about
    path(
        'about/',
        views.about,
        name='about'
    ),
    # post feed 
    path(
        'feed/',
        PostFeed(),
        name='post_feed'
    ),
    # post detail
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post_slug>/',
        views.post_detail,
        name='post_detail'
    ),
    # post list
    path(
        '',
        views.post_list,
        name='post_list'
    ),
]
