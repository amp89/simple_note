from django.urls import path
from django.urls import include
from interface import views
from django.views.generic import TemplateView

urlpatterns = [
    path("privacy/", TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path("tos/", TemplateView.as_view(template_name='tos.html'), name='tos'),
    path("", views.HomeView.as_view(), name='home'),
    
]
