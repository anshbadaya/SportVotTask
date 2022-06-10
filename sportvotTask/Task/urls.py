from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_View, name='page_View'),
]