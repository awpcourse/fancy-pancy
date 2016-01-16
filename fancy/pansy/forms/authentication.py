from django.db.models.fields.files import ImageField
from django.forms import Form, CharField, PasswordInput, EmailField, \
    BooleanField
from fancy.settings import MEDIA_ROOT

class UserSigninForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserSignupForm(Form):
    username = CharField(max_length=30)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = EmailField()
    password = CharField(max_length=30, widget=PasswordInput)
    retype_password = CharField(max_length=30, widget=PasswordInput)

