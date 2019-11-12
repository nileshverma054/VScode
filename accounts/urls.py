from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.signup, name='signup'),
    path('signup_user/',views.signup_user, name='signup_user'),
    path('login/',views.login, name='login'),
    path('login_user/',views.login_user, name='login_user'),
    path('logout/',views.logout, name='logout'),
]