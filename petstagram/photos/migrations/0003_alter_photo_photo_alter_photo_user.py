# Generated by Django 4.2.7 on 2023-12-05 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', validators=[petstagram.photos.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]