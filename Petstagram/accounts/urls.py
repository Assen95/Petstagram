from django.urls import path, include

from Petstagram.accounts.views import register, login, profile_edit, profile_details, profile_delete

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile-details'),
        path('edit/', profile_edit, name='profile-edit'),
        path('delete/', profile_delete, name='profile-delete')
    ]))
]