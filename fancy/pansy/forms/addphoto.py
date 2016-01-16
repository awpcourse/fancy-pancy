from django.db.models.fields.files import ImageField
from django.forms import Form, CharField, BooleanField, FileInput, FileField

from fancy.settings import MEDIA_ROOT


class AddPhotoForm(Form):
    name = CharField(max_length=50)
    description = CharField(max_length=200)
    public = BooleanField()
    image = FileField()
