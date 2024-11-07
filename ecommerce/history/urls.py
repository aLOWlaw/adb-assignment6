from django.urls import path
from .views import HistoryCreateView


urlpatterns = [
    path('api/like/', HistoryCreateView.as_view(), name='create_like'),
]
