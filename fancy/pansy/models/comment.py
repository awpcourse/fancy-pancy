from django.contrib.auth.models import User
from django.db import models
import pansy.models.photo as photo

class Comment(models.Model):
    text = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(photo.Photo)
    owner = models.ForeignKey(User)

