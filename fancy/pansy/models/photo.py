from django.db import models
from fancy.settings import MEDIA_ROOT
from django.contrib.auth.models import User

class Photo(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    image = models.FileField(upload_to=MEDIA_ROOT)
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()
    owner = models.ForeignKey(User)

