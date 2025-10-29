from django.urls import path
from . import views

app_name = 'bg1'
urlpatterns = [
    path('', views.CharListView.as_view(), name='list'),
    path('<int:pk>/', views.CharDetailView.as_view(), name='detail'),
]
