from django import forms

from petstagram.photos.models import Photo
from petstagram.pets.models import Pet

labels = {
    'pet_image': 'Photo file',
    'description': 'Description',
    'location': 'Location',
    'tagged_pets': 'Tag Pets'
}

class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        exclude = ['user']
        labels = labels

    def __init__(self, user, *args, **kwargs):
        super(PhotoAddForm, self).__init__(*args, **kwargs)
        self.fields['tagged_pets'].queryset = Pet.objects.filter(user=user)


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'location', 'tagged_pets']
        exclude = ['photo']
        labels = labels

    def __init__(self, user, *args, **kwargs):
        super(PhotoEditForm, self).__init__(*args, **kwargs)
        self.fields['tagged_pets'].queryset = Pet.objects.filter(user=user)
