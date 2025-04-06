# prediction/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('prediction/', views.prediction, name='prediction'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='prediction/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='prediction/logout.html'), name='logout'),
]

# Add static URL mapping in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
