from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('comments/', views.get_comments, name='get_comments'),
    path('custom-comments/', views.get_custom_comments, name='custom-comments'),
]
