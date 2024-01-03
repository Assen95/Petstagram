from django.contrib.auth import get_user_model
from django.db import models

from petstagram.accounts.models import PetstagramUser
from petstagram.photos.models import Photo

User = get_user_model()


class Comment(models.Model):
    text = models.CharField(
        max_length=300,
    )
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ["-date_time_of_publication"]


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
