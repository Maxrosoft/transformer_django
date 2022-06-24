from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class MainData(models.Model):
    title = models.CharField(max_length=25)
    info = models.TextField()
    image_url = models.TextField()

    objects = models.Manager()
    published = PublishedManager()


class AboutUsData(models.Model):
    adds = models.CharField(max_length=250)
    contacts = models.CharField(max_length=250)

    objects = models.Manager()
    published = PublishedManager()