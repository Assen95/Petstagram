from django.shortcuts import render


def register(request):
    return render(request, template_name='accounts/register-page.html')


def login(request):
    return render(request, template_name='accounts/login-page.html')


def profile_details(request):
    return render(request, template_name='accounts/profile-details-page.html')


def profile_edit(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def profile_delete(request):
    return render(request, template_name='accounts/profile-delete-page.html')

