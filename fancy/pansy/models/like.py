from django.contrib.auth.models import User
from django.db import models
import pansy.models.photo as photo


class Like(models.Model):
    photo = models.ForeignKey(photo.Photo)
    # owner = models.ForeignKey(User)
