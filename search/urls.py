from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('thebestwonders/', views.theBestWonders, name='thebestwonders'),
    path('searchpage/<str:typestring>/', views.searchResult, name='searchpage'),
    path('searchpage/', views.searchHome, name = 'searchhome')
]