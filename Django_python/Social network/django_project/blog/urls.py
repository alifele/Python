from django.urls import path
from . import views
#import .views



urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.subhome, name='blog-about')
]
