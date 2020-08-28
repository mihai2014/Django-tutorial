from django.db import models

class Books(models.Model):

    title = models.CharField(max_length = 200)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url1(self):
        return f"/generic-views/detail-book-id/{self.id}/"

    def get_absolute_url2(self):
        return f"/generic-views/detail-book-slug/{self.slug}/"


# see /home/mihai/all/data/work2020/django/dj_test/geeks/models.py :

from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender = Books)
