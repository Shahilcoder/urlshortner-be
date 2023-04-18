from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.generateShortUrl, name='shorten'),
    path('<str:url>', views.getLongUrl, name='long')
]