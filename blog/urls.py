from django.urls import path
from .feeds import PostFeed
from . import views

app_name =  'blog'

urlpatterns = [
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
