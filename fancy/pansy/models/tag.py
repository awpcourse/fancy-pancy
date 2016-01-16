from django.contrib.auth.models import User
from django.db import models
import pansy.models.photo as photo


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False)


class TagToPhoto(models.Model):
    photo = models.ForeignKey(photo.Photo)
    tag = models.ForeignKey(Tag)
