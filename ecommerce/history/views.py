from rest_framework import views, generics
from .models import HistoryModel
from .serializers import HistoryModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class HistoryCreateView(generics.CreateAPIView):
    queryset = HistoryModel.objects.all()
    serializer_class = HistoryModelSerializer
    permission_classes = [AllowAny]
    