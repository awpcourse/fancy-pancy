from django.shortcuts import render
from pansy.forms.search import SearchForm
from pansy.models.photo import Photo
import unicodedata

def search_view(request):
    if request.method == 'POST':
        search_key = request.POST['searchField']
        form = SearchForm({"searchField":search_key})
        if not form.is_valid():
            return render(request, 'search.html', {'searchform': form})
        
        data = form.cleaned_data
        key = unicodedata.normalize('NFKD', search_key).encode('ascii','ignore')
        #photos_tag = Photo.objects.filter(tagtophoto__icontains=key)
        photos_name = Photo.objects.filter(name__icontains=key)
        photos_description = Photo.objects.filter(description__icontains=key)
        photos = [ photos_name, photos_description]
        
        return render(request, 'search.html', {'results': ""})
    
    elif request.method == "GET":
        form = SearchForm()
        return render(request, 'search.html' ,{'searchform': form})