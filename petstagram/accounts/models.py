from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators

from petstagram.accounts.validators import alphanumeric


class PetstagramUser(auth_models.AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    ]

    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            alphanumeric,
        ),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            alphanumeric,
        ),
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        # TODO: change it, when you re-migrate database and delete local migrations
        # blank=True,
        # null=True,
    )

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username
