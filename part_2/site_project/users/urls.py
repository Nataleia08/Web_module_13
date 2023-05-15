from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.log_out_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('script/', views.script, name='script'),
]