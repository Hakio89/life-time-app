from django.urls import path
from working_time import views

urlpatterns = [
    path('main/', views.LifeTimeView.as_view(), name='life_time_view'),
    # Define your URL patterns here
    # Example:
    # path('some-path/', some_view, name='some_view_name'),
]