from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.accounts.models import PetstagramUser
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size

User = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(
        validators=(validate_file_size,),
        null=False,
        blank=True
    )
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )