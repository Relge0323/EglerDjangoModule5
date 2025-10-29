from django.views.generic import TemplateView

class HomeDetailView(TemplateView):
    template_name = 'index.html'