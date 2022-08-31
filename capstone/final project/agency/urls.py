from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plans', views.plans, name='plans'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
]
