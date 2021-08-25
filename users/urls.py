from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registermanager/', views.registermanager, name='register-manager'),
    path('registereditor/', views.registereditor, name='register-editor'),
     path('registerlibrarian/', views.registerlibrarian, name='register-librarian'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('deactivate/', views.deactivate, name="deactivate"),
    path('profile/', views.profile, name='profile'),
    path('login/', views.MPLLLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
