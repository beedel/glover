from django.urls import path

from . import views

app_name = "glover"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('discover/', views.discover, name='discover'),
    path('discover/<str:username>/', views.discover_profile, name='discover_profile'),

    path('matches/', views.matches, name='matches'),
    path('matches/<str:username>/', views.match_profile, name='match-profile'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('profile/edit-photos/', views.edit_photos, name='edit-photos'),

    path('messages/', views.messages, name='messages'),
    path('messages/<str:username>/', views.user_messages, name='user-messages'),
    
    # urls without templates
    path('discover/users/<str:profile2>/like/', views.like, name='like'),
    path('discover/users/<str:profile2>/unmatch/', views.unmatch, name='unmatch'),
    path('discover/users/<str:profile2>/block/', views.block, name='block'),
    path('profile/edit/delete-account/', views.delete_account, name='delete-account'),
]

ajax_urls = [
    path('ajax/delete-photo/', views.delete_photo, name='delete-photo'),
]

urlpatterns += ajax_urls