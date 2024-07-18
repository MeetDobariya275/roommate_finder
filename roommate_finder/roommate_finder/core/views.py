from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Listing, Message
from .forms import ProfileForm, ListingForm, MessageForm

def homepage_view(request):
    return render(request, 'core/home.html')


def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'core/profile_detail.html', context)

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'core/listing_detail.html', context)

def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    context = {'message': message}
    return render(request, 'core/message_detail.html', context)

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect('listing-detail', listing_id=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'core/create_listing.html', {'form': form})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-detail', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})