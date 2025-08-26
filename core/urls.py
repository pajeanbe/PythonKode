from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('<slug:topic_slug>/', views.topic_detail, name='topic_detail'),
    path('<slug:topic_slug>/<slug:article_slug>/', views.article_detail, name='article_detail'),
]
