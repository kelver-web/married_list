from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('gifts/', views.gift_list, name='gift_list'),
    path('gifts/reserve/<int:gift_id>/', views.reserve_gift, name='reserve_gift'),
    path('our-love-story/', views.our_love_story, name='our_love_story'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),

    # autenticação
    path('register/', views.guest_register, name='guest_register'),
    path('login/', views.guest_login, name='guest_login'),
    path('logout/', views.guest_logout, name='guest_logout'),
]