from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'), # тут пустая страница, потому, что пользователь уже перешёл на /new/ когда
    # переходил по ссылке из основного urls.py
]
