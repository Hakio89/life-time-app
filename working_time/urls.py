from django.urls import path
from working_time import views

urlpatterns = [
    path('', views.LifeTimeView.as_view(), name='life_time_view'),
    path('o-nas/', views.AboutUsView.as_view(), name='about_us_view'),
    path('panel/', views.LifeTtimeDashboardView.as_view(), name='dashboard_view'),
    path('projekty/', views.ProjectsView.as_view(), name='projects_view'),
    path('wpisy-czasu/', views.TimeEntryView.as_view(), name='time_entry_view'),
    path('raporty/', views.WorkingTimeReportsView.as_view(), name='reports_view'),
    path('stoper/', views.TimerView.as_view(), name='timer_view'),
    path('dodaj-wpis/', views.AddTimeEntryView.as_view(), name='add_time_entry_view'),
    # Define your URL patterns here
    # Example:
    # path('some-path/', some_view, name='some_view_name'),
]