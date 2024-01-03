from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class AdminPhoto(admin.ModelAdmin):
    list_display = ('id', 'description', 'location', 'date_of_publication', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ", ".join([pet.name for pet in obj.tagged_pets.all()])