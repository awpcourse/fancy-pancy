from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from pansy.models.photo import Photo
from pansy.forms.addphoto import AddPhotoForm
from fancy.pansy.forms.comment import CommentForm
from fancy.pansy.models.comment import Comment


class CommentView(TemplateView):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        ph = Photo.objects.get(pk=pk)

        if form.is_valid():
            text = form.cleaned_data['text']
            comment = Comment(text=text, owner=request.user, photo=ph)
            comment.post_id = pk
            comment.save()