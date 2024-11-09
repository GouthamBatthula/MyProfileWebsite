from django.contrib import admin
from django.urls import path
from app_79_3 import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='profile'),  # Homepage
    path('contact/', views.contact, name='contact'),  # Contact page
]
