from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="Shop Home"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Tracking Status"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productView, name="Product View"),
    path("checkout/", views.checkout, name="Checkout"),
    path("about/", views.about, name="About Us")
]
