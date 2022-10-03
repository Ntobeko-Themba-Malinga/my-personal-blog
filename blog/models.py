from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    # managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Project(models.Model):
    thumbnail = models.ImageField(upload_to='project_thumbnails')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = HTMLField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    status = models.CharField(
        max_length=2,
        choices=Post.Status.choices,
        default=Post.Status.DRAFT
    )
    created = models.DateTimeField(auto_now_add=True)

    # Managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:project_detail',
            args=[
                self.slug
            ]
        )


class About(models.Model):
    title = models.CharField(max_length=250)
    body = HTMLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
