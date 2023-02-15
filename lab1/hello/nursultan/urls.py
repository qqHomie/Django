from django.urls import path, include

from . import views

app_name = 'nursultan'

urlpatterns = [
    path('', views.index, name='index')
]