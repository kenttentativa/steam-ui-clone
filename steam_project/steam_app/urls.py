from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home Page
    path('elden-ring/', views.elden_ring, name='elden-ring'),
    path('dota-2/', views.dota_2, name='dota-2'),
    path('assassins-creed/', views.assassins_creed, name='assassins-creed'),
    path('god-of-war/', views.god_of_war, name='god-of-war'),
    path('browse-games/', views.browse_games, name='browse-games'),
    path('red-dead-redemption/', views.red_dead_redemption, name='red-dead-redemption'),
    path('cyberpunk/', views.cyberpunk, name='cyberpunk'),
    path('the-witcher-3/', views.the_witcher_3, name='the_witcher_3'),
    path('final-fantasy/', views.final_fantasy, name='final_fantasy'),
    path('community/', views.community, name='community'), 
    path('about/', views.about, name='about'), 
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),  # Login Page
    path('logout/', views.logout_view, name='logout'),  # Logout Page
]
