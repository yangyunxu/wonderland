from django.urls import path
from home import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),

]