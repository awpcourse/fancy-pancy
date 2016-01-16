from django.forms import Form, CharField, PasswordInput


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)