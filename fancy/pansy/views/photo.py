from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from pansy.models.photo import Photo
from pansy.models.comment import Comment
from pansy.models.tag import Tag


class PhotoView(TemplateView):
    def get(self, request, pk):
        ph = Photo.objects.get(pk=pk)
        comments = ph.comment_set.all().order_by('-date_added')
        tags = [t.tag for t in ph.tagtophoto_set.all()]
        likes = ph.like_set.count()

        context = {'photo': ph, 'comments': comments, 'tags': tags,
                   'likes': likes}

        return render(request, 'show_photo.html', context)
