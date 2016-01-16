from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from pansy.models.photo import Photo
from pansy.forms.addphoto import AddPhotoForm


class PhotoView(TemplateView):
    def get(self, request, pk):
        ph = Photo.objects.get(pk=pk)
        comments = ph.comment_set.all().order_by('-date_added')
        tags = [t.tag for t in ph.tagtophoto_set.all()]
        likes = ph.like_set.count()

        path = ph.image.url.split('/')[-1]
        context = {'photo': ph, 'comments': comments, 'tags': tags,
                   'likes': likes, 'path': path}

        return render(request, 'show_photo.html', context)


class AddPhotoView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = AddPhotoForm()
        context = {'form': form}

        return render(request, 'add-photo.html', context)

    def post(self, request):
        form = AddPhotoForm(request.POST)
        print(form.is_valid())
        # if not form.is_valid():
        #     context = {'form': form}
        #     return render(request, 'add-photo.html', context)
        name = request.POST['name']
        description = request.POST['description']
        public = request.POST['public']
        image = request.FILES['image']
        owner=request.user

        photo = Photo(name=name, description=description, public=public, image=image, owner=owner)
        photo.save()

        return redirect('/photo/' + str(photo.id))

