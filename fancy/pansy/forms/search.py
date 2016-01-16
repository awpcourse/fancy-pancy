from django.forms import Form, CharField

class SearchForm(Form):
    searchField = CharField(max_length=20)
