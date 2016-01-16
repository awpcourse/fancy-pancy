from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from pansy.models.photo import Photo
from pansy.models.comment import Comment
from pansy.models.tag import Tag


class RecentPhotosView(TemplateView):
    def get(self, request):
        photos = Photo.objects.filter(public=True).order_by('-date_added')
        ph = [(a, a.image.url.split('/')[-1]) for a in photos]
        context = {'photos': ph}

        return render(request, 'show_photos.html', context)