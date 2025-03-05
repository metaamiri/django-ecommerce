from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *


def index(request):
    context = {"listings": Listing.objects.all()}
    return render(request, "auctions/index.html", context)

def listing_page(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    current_price = listing.price.last().bid  # Get the highest bid
    comments = listing.comments.all()
    is_owner = request.user == listing.user
    # in_watchlist = request.user.is_authenticated and request.user.watchlist.filter(id=listing.id).exists()
    
    if request.method == "POST":
        # if "watchlist" in request.POST:
        #     if in_watchlist:
        #         request.user.watchlist.remove(listing)
        #         messages.success(request, "Removed from Watchlist")
        #     else:
        #         request.user.watchlist.add(listing)
        #         messages.success(request, "Added to Watchlist")
        #     return redirect("auctions/listing_detail.html", listing_id=listing.id)
        
        if "bid" in request.POST:
            if request.user.is_authenticated:
                bid_amount = float(request.POST.get("bid_amount"))
                if current_price and bid_amount <= current_price:
                    messages.error(request, "Your bid must be higher than the current price.")
                elif bid_amount < 1:  # Assuming 1 as the minimum starting bid
                    messages.error(request, "Your bid must be at least 1.")
                else:
                    Price.objects.create(listing=listing, user=request.user, bid=bid_amount)
                    messages.success(request, "Bid placed successfully!")
                return redirect("auctions/listing_detail.html", listing_id=listing.id)
        
        elif "close_auction" in request.POST and is_owner:
            listing.active = False
            listing.save()
            messages.success(request, "Auction closed.")
            return redirect("auctions/listing_detail.html", listing_id=listing.id)
        
        elif "comment" in request.POST:
            comment_text = request.POST.get("comment")
            if comment_text:
                Comment.objects.create(listing=listing, user=request.user, comment=comment_text)
                messages.success(request, "Comment added.")
            return redirect("auctions/listing_detail.html", listing_id=listing.id)

    return render(request, "auctions/listing_detail.html", {
        "listing": listing,
        "current_price": current_price,
        "comments": comments,
        "is_owner": is_owner,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
