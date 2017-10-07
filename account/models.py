from django.db import models
from django.contrib.auth.models import User

from article.models import Post
from collection.models import Website


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    signature = models.CharField(max_length=200, blank=True)
    birth = models.DateField()
    collections = models.ManyToManyField(Website)
    likes = models.ManyToManyField(Post)

    class Meta:
        pass

    def __str__(self):
        return self.user.username
