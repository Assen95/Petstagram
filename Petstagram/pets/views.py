from django.shortcuts import render


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def details_pet(request, pk, pet_name):
    return render(request, template_name='pets/pet-details-page.html')


def edit_pet(request, pk, pet_name):
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request, pk, pet_name):
    return render(request, template_name='pets/pet-delete-page.html')