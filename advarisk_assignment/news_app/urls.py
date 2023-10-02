from django.urls import path
from . import views

urlpatterns = [
    path('', views.handlelogin,name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.handlelogout, name='logout'),
    path('search/', views.search_news, name='search_news'),
    path('results/<int:keyword_id>/', views.view_results, name='view_results'),
]
