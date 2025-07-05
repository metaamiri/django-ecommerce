from django.urls import path
from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing-page/<int:listing_id>", views.listing_page, name="listing_page"),
    path("change-watchlist/", views.change_watchlist, name="change_watchlist"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category_name>", views.category_listing, name="category_listings"),
    path("create-listing/", views.create_listing, name="create_listing"),
]
