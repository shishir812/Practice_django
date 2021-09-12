from django.urls import path
from basic_app import views



urlpatterns = [

    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('special', views.special, name='special'),
]