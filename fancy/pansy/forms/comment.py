from django.db.models.fields.files import ImageField
from django.forms import Form, CharField, BooleanField, FileInput, FileField, \
    Textarea

from fancy.settings import MEDIA_ROOT


class CommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 80, 'rows': 5}),
        label="Enter your comment here")