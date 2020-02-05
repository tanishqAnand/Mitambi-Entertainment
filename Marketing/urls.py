from django.urls import path, include
from Marketing import views

urlpatterns = [
    path('join/', views.join, name='join-us'),
    path('about-us/', views.about_us, name='about-us'),
    path('influencer/', views.influencer, name='influencer'),
    path('brand/', views.brand, name='brand'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('', views.home, name='home'),
]
