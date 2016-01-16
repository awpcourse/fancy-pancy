from django.shortcuts import render
from django.db.models import Q
from pansy.forms.search import SearchForm
from pansy.models.photo import Photo
from pansy.models.tag import Tag
from pansy.models.tag import TagToPhoto
import unicodedata

def search_view(request):
    if request.method == 'POST':
        search_key = request.POST['searchField']
        form = SearchForm({"searchField":search_key})
        if not form.is_valid():
            return render(request, 'show_photos.html', {'searchform': form})
        
        data = form.cleaned_data
        key = unicodedata.normalize('NFKD', search_key).encode('ascii','ignore')
    
        photos = Photo.objects.filter(Q(name__icontains=key) | Q(description__icontains=key),)
        request.photos = photos
        return render(request, 'show_photos.html', {'photos': photos})
    
    elif request.method == "GET":
        form = SearchForm()
        return render(request, 'show_photos.html', {'searchform': form})