from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('profile/<str:username>/', views.profile_detail, name='profile-detail'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing-detail'),
    path('message/<int:message_id>/', views.message_detail, name='message-detail'),
    path('create_listing/', views.create_listing, name='create-listing'),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
]
