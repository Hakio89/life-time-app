from django.shortcuts import render
from django.views.generic import TemplateView

class LifeTtimeDashboardView(TemplateView):
    template_name = 'working_time/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context
    
class ProjectsView(TemplateView):
    template_name = 'working_time/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projekty'
        return context
    
class TimeEntryView(TemplateView):
    template_name = 'working_time/timeentries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Time Entry'
        return context

class WorkingTimeReportsView(TemplateView):
    template_name = 'working_time/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reports'
        return context
    
class TimerView(TemplateView):
    template_name = 'working_time/timer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stoper'
        return context
    
class AddTimeEntryView(TemplateView):
    template_name = 'working_time/addentries..html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dodan wpis'
        return context

class LifeTimeView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Life Time App'
        return context
    
class AboutUsView(TemplateView):
    template_name = 'description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'O nas'
        return context