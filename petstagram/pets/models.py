from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from petstagram.accounts.models import PetstagramUser

User = get_user_model()


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    personal_photo = models.URLField(
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)