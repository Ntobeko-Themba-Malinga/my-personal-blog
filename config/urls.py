from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from blog.sitemaps import PostSitemap
from config.settings import MEDIA_ROOT

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

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
