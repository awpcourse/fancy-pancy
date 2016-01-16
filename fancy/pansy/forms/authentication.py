from django.forms import Form, CharField, PasswordInput, EmailField


class UserSigninForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)

class UserSignupForm(Form):
    username = CharField(max_length=30)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = EmailField()
    password = CharField(max_length=30)

