from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='core_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('criar-conta/', views.criar_conta, name='criar_conta')
    # path('logout/', views.logout, name='core_logout')
]
