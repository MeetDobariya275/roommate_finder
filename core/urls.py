from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('', views.homepage_view, name='home'),
    path('create_listing/', views.create_listing, name='create-listing'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing-detail'),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
    path('profile/<str:username>/', views.profile_detail, name='profile-detail'),
    path('search/', views.search_listings, name='search-listings'),
]
