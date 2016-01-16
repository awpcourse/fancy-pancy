from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    name = models.TextField()
    description = models.TextField()
    path = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True)
    public = models.BooleanField()

    # tags
    # comments
    # maybe views

    # owner = models.ForeignKey(User)

