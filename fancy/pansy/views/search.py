from django.shortcuts import render
from pansy.forms.search import SearchForm

def search_view(request):
    if request.method == 'POST':
        search_key = request.POST['searchField']
        form = SearchForm({"searchField":search_key})
        if not form.is_valid():
            return render(request, 'search.html', {'searchform': form})
        
        data = form.cleaned_data
        searchField = data['searchField'].values()[0]
        photos_tag = Photo.objects.filter(tags__icontains=searchField)
        photos_name = Photo.objects.filter(name__icontains=searchField)
        photos_description = Photo.objects.filter(description__icontains=searchField)
        photos = [photos_tag, photos_name, photos_description]
    
        return render(request, 'search.html', {'results': photos})
    
    elif request.method == "GET":
        form = SearchForm()
        return render(request, 'search.html' ,{'searchform': form})