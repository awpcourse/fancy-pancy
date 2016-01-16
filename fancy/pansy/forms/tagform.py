from django.forms import Form, CharField


class TagForm(Form):
    name = CharField(max_length=20)
