from django.urls import path
from myaccount import views


app_name = 'myaccount'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.myaccount, name='myaccount'),
]