from rest_framework import permissions, viewsets

from .models import *
from .serializer import *


class ReclamadaViewSet(viewsets.ModelViewSet):
    queryset = Reclamadas.objects.all()
    serializer_class = ReclamadasSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReclamanteViewSet(viewsets.ModelViewSet):
    queryset = Reclamantes.objects.all()
    serializer_class = ReclamantesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProcessosViewSet(viewsets.ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [permissions.IsAuthenticated]


class AndamentosViewSet(viewsets.ModelViewSet):
    queryset = Andamentos.objects.all()
    serializer_class = AndamentosSerializer
    permission_classes = [permissions.IsAuthenticated]