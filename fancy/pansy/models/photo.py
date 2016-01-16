from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    path = models.CharField(max_length=100, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()

    # tags
    # comments
    # maybe views

    # owner = models.ForeignKey(User)

