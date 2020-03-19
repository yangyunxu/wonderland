from django.urls import path
from category import views

app_name = 'category'

urlpatterns = [
    path('category/<slug:category_name_slug>/', views.category, name='category'),
    path('categories/', views.category_select, name='categories'),
    path('page/<slug:page_name_slug>/', views.page, name='page'),
    path('submitComment/', views.submitComment, name='submitComment')
]