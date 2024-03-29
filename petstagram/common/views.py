from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url

from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo
from petstagram.common.forms import CommentForm, SearchForm

User = get_user_model()


def homepage(request):
    all_photos = Photo.objects.all()

    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    if request.user.is_authenticated:
        all_liked_photos_by_request_user = [like.to_photo_id for like in request.user.like_set.all()]
        context['all_liked_photos_by_request_user'] = all_liked_photos_by_request_user

    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details-photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
