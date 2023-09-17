from rest_framework import viewsets
from apps.watch.permissions import IsAdminUserOrReadOnly
from .models import Watch
from .serializers import WatchSerializer


class WatchListCreateAPIView(viewsets.ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class WatchRetrieveUpdateDestroyAPIView(viewsets.ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = [IsAdminUserOrReadOnly]