from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.username}"
    
class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=32)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    first_bid = models.DecimalField(max_digits=10, decimal_places=2,default=0)
   

    def __str__(self):
        return f"{self.title} ({self.active})"
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ManyToManyField(Listing, blank=True, related_name="watchlist")
    
    def __str__(self):
        return f"{self.user} watchlist"
    
    
class Price(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="price")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"${self.bid} {self.listing} by {self.user} "
    


class Category(models.Model):
    listing = models.ManyToManyField(Listing, blank=True, related_name="categories")
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"
    
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment}"