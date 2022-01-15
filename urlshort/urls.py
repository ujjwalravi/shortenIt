from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random/', views.random, name='genrandom'),
    path('custom/', views.custom, name='gencustom'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('r/<str:u>/', views.shurl, name='shurl'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]