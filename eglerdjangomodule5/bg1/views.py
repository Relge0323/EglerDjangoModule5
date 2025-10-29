from django.views.generic import ListView, DetailView
from .models import Character

# Create your views here.
class CharListView(ListView):
    model = Character
    template_name = 'bg1/char_list.html'


class CharDetailView(DetailView):
    model = Character
    template_name = 'bg1/char_detail.html'
    context_object_name = 'char'