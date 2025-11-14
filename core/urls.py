from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='core_login'),
    path('logout/', views.logout, name='core_logout')
]
