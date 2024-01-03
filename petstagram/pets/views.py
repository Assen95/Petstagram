from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from petstagram.pets.models import Pet
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.utils import get_pet_by_slug_and_username

User = get_user_model()


@login_required
def add_pet(request):
    form = PetAddForm()
    current_user = request.user.pk

    if request.method == 'POST':
        form = PetAddForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile-details', pk=current_user)
    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


@login_required
def details_pet(request, username, pet_name):
    pet = get_pet_by_slug_and_username(pet_name, username)
    all_photos = pet.photo_set.all()
    is_owner = request.user = pet.user
    print(f'Logged in User: {request.user}')
    print(f'Page owner: {pet.user}')
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'is_owner': is_owner,
    }

    return render(request, 'pets/pet-details-page.html', context)


@login_required
def edit_pet(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    form = PetEditForm(instance=pet)

    if request.method == 'POST':
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()

            return redirect('details-pet', username=username, pet_name=pet_name)

    context = {
        'form': form,
        'username': username,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


@login_required
def delete_pet(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    form = PetDeleteForm(instance=pet)
    current_user = request.user.pk

    if request.method == 'POST':
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()

            return redirect('profile-details', pk=current_user)

    context = {
        "form": form,
        "username": username,
        "pet_name": pet_name,
    }

    return render(request, 'pets/pet-delete-page.html', context)
