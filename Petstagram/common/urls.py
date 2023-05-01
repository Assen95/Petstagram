from django.urls import path, include

from Petstagram.common.views import index

urlpatterns = [
    path('', index, name='index'),
]