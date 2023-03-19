from django.urls import path
from .import views


app_name = 'auth_user'
urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('user_logout/', views.user_logout, name='logout'),
    path('registration/', views.registration, name='registration'),
]