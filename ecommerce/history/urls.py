from django.urls import path
from .views import HistoryCreateView


urlpatterns = [
    path('api/action/', HistoryCreateView.as_view(), name='create_action'),
]
