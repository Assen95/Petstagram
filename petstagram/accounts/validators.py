from django.core import validators

alphanumeric = validators.RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed')