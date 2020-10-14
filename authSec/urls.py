from django.urls import path
from . import views

urlpatterns = [
    path('login', views.authLogin, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
    path('logout/', views.authLogout, name='logout'),
]
