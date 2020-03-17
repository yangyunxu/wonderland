from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('thebestwonders/', views.theBestWonders, name='thebestwonders'),
    path('searchpage/', views.searchResult, name='searchpage'),
]