from django.urls import path
from . import views

urlpatterns = [
    path('summary', views.data_summary, name='datasummary-summary'),
]
