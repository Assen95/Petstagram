from django.conf import settings
from django.forms import ModelForm
from django import forms

from petstagram.pets.models import Pet


class PetBasicForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            # 'date_of_birth': forms.DateInput(
            #     attrs={'placeholder': 'dd/mm/yyyy', 'type': 'text', 'readonly''onfocus': "(this.type='date')" }
            # ),
            'date_of_birth': forms.DateInput(attrs={
                # 'placeholder': 'dd/mm/yyyy',
                'type': 'date',
            }),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }
        labels = {
            'name': "Pet Name",
            'date_of_birth': "Date of Birth",
            'personal_photo': "Link to Image",
        }


class PetAddForm(PetBasicForm):
    pass


class PetEditForm(PetBasicForm):
    pass


class PetDeleteForm(PetBasicForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
