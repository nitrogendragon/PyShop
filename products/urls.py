from django.urls import path
from . import views

#setting up paths so django knows what view to show based on what we enter after products/
# so products/   will take us to views.index
# and products/new will take us to views.new and thusly show us the respective pages
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]