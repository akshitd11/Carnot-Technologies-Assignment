from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),    
    path("search/", views.search, name= "search"),
    path("searchResults/<str:query>/", views.searchUrlByName, name="searchResults"),
    path("searchResults/", views.searchResults, name="searchResults"),
    path("uploadcsv/", views.uploadcsv, name = "uploadcsv")
    
]
