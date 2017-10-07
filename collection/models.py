from django.db import models

from main.models import Category, Tag


class Website(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    category = models.ForeignKey(Category)
    collected = models.IntegerField(default=0)
    describe = models.CharField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-collected']
