from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, ListingForm, ProfileForm
from .models import Profile, Listing
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)  # Create an empty profile for the new user
            login(request, new_user)
            return redirect('home')  # Make sure 'home' is defined in your URL patterns
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

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

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'core/listing_detail.html', context)

def homepage_view(request):
    return render(request, 'core/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'core/logout.html')

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-detail', username=request.user.username)  # Ensure this URL pattern exists
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})
    
@login_required
def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'core/profile_detail.html', context)

def search_listings(request):
    query = request.GET.get('q')  # Get the search query from GET parameters
    if query:
        listings = Listing.objects.filter(title__icontains=query)
    else:
        listings = Listing.objects.all()  # Or handle the case where there's no query
    return render(request, 'core/search_results.html', {'listings': listings})

def some_view(request):
    return HTTPResponse("This is the admin view.")