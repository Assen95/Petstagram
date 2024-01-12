from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views import generic as views

from petstagram.photos.models import Photo
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm

User = get_user_model()

# @login_required
# class PhotoAddView(views.CreateView):
#     template_name = 'photos/photo-add-page.html'
#     form_class = PhotoAddForm
#
#     def get_success_url(self):
#         return reverse('details-photo', kwargs={
#             'pk': self.object.pk
#         })
#
#     def get_form(self, *args, **kwargs):
#         form = super().get_form(*args, **kwargs)
#         form.instance.user = self.request.user
#         return form


@login_required
def add_photo(request):

    form = PhotoAddForm(request.user, request.FILES)
    if request.method == 'POST':
        form = PhotoAddForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('homepage')

    context = {
        'form': form
    }

    return render(request, 'photos/photo-add-page.html', context)


@login_required
def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.user, instance=photo)

    if request.method == "POST":
        form = PhotoEditForm(request.user, request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details-photo', pk=pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


@login_required
def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    photo_is_liked_by_user = likes.filter(user=request.user)
    comments = photo.comment_set.all()
    photo_owner = photo.user
    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
        'photo_is_liked_by_user': photo_is_liked_by_user,
        'photo_owner': photo_owner
    }

    if photo_owner.first_name and photo_owner.last_name:
        context['both_names'] = photo_owner.first_name + ' ' + photo_owner.last_name

    return render(request, 'photos/photo-details-page.html', context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('homepage')
