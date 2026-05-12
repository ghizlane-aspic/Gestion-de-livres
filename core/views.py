from rest_framework import viewsets, filters
from .models import Livre
from .serializers import LivreSerializer


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titre', 'auteur', 'isbn']
    ordering_fields = ['titre', 'auteur', 'prix', 'date_publication']
    ordering = ['titre']
