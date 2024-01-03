from petstagram.pets.models import Pet
from django.shortcuts import get_object_or_404


def get_pet_by_slug_and_username(pet_name, username):
    return Pet.objects\
        .filter(slug=pet_name, user__username=username)\
        .get()
