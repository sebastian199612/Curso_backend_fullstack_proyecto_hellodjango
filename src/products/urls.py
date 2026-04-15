from django.contrib import admin
from django.urls import path  
from django.views.generic import TemplateView ,RedirectView

from products import views
from products.views import (
    ProductListView,
    ProductDetailView , 
    DigitalProduct , 
    ProtectedListView,
    ProtectedProductDetailView,
    ProductIDRedirectView,
    ProductRedirectView,
    ProtectedProductCreateView,
    ProtectedProductUpdateView, 
    ProtectedProductDeleteView  
    )

urlpatterns = [ 
    path("admin/" , admin.site.urls),
    path("aboout-us", RedirectView.as_view(url="/products/about/")),
    path("about/", TemplateView.as_view(template_name="about.html")),
    path("team/", TemplateView.as_view(template_name="team.html")),
    path("products/", ProductListView.as_view()),
    path("digital-products/", DigitalProduct.as_view()),
    path("products/<int:pk>", ProductDetailView.as_view()),
    path("products/<slug:slug>",ProductDetailView.as_view()),
    path("p/<int:pk>", ProductIDRedirectView.as_view()),
    path("p/<slug:slug>",ProductRedirectView.as_view()),
    path("my-products/",ProtectedListView.as_view()),####
    path("my-products/<slug:slug>",ProtectedProductDetailView.as_view()),
    #path("my-products/create/", ProtectedProductCreateView.as_view()),
    #path("my-products/<slug:slug>/", ProtectedProductUpdateView.as_view()),
    #path("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()),

    ]