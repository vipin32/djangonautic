from django.urls import path

from . import views

app_name='articles'

urlpatterns = [
    path('', views.index, name='list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]
