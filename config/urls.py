from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'sitemap.xml/',
        sitemap,
        { 'sitemaps': sitemaps },
        name='sitemap'
    ),
    path(
        '',
        include('blog.urls', namespace='blog'),
    )
]
