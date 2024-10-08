from django.urls import path

from . import views

urlpatterns = [
    path('pon/', views.emply_list, name='emply_list')	
]