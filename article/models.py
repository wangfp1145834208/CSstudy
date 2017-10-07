from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.html import strip_tags
import markdown

from main.models import Category, Tag


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    mark_down = models.BooleanField(default=False)
    auth = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:100]
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('article:post_detail', args=(self.pk,))
