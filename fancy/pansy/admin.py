from django.contrib import admin
from pansy.models import photo
from pansy.models import tag
from pansy.models import comment
# Register your models here.

admin.site.register(photo.Photo)
admin.site.register(tag.Tag)
admin.site.register(comment.Comment)