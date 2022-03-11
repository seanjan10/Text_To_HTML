from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path("converted/", views.converted, name='converted')
]