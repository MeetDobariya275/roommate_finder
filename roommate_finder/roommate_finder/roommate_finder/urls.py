from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='home'),
    path('profile/<str:username>/', views.profile_detail, name='profile-detail'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing-detail'),
    path('message/<int:message_id>/', views.message_detail, name='message-detail'),
    path('create_listing/', views.create_listing, name='create-listing'),  # New path for creating a listing
    path('edit_profile/', views.edit_profile, name='edit-profile'),        # New path for editing a profile
]
