from django.urls import path
from . import views
from personal_assignments.cookie import toggle_theme

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('toggle_theme/', toggle_theme, name='toggle_theme'),
]
