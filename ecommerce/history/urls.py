from django.urls import path
from .views import HistoryCreateView, BookRecommendationsView


urlpatterns = [
    path('api/action/', HistoryCreateView.as_view(), name='create_action'),
    path('recommendations/category/', BookRecommendationsView.as_view(), name='user-category-recommendations'),

]
