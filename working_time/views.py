from django.shortcuts import render
from django.views.generic import TemplateView

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