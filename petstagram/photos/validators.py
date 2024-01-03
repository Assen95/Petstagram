from django.core.exceptions import ValidationError


def validate_file_size(file):
    if file.size > 5242880:
        raise ValidationError('The maximum file size cannot exceed 5MB')
