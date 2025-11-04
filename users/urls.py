from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('logowanie/', views.LoginView.as_view(), name='login_view'),
    path('rejestracja/', views.RegisterView.as_view(), name='register_view'),
    path('wyloguj/', views.LogoutView.as_view(), name='logout_view'),
    # Define your URL patterns here
    # Example:
    # path('some-path/', some_view, name='some_view_name'),
]