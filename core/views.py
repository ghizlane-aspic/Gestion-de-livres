from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rest_framework import viewsets, filters

from .models import Livre
from .serializers import LivreSerializer


# ── API (Phase 1) ────────────────────────────────────────────────────────────

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titre', 'auteur', 'isbn']
    ordering_fields = ['titre', 'auteur', 'prix', 'date_publication']
    ordering = ['titre']


# ── Interface web (Phase 2) ──────────────────────────────────────────────────

class LivreListView(ListView):
    model = Livre
    template_name = 'core/livre_list.html'
    context_object_name = 'livres'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        qs = Livre.objects.all().order_by('titre')
        if query:
            qs = qs.filter(Q(titre__icontains=query) | Q(auteur__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('q', '')
        ctx['total'] = self.get_queryset().count()
        ctx['total_all'] = Livre.objects.count()
        ctx['disponibles_count'] = Livre.objects.filter(disponible=True).count()
        ctx['non_disponibles_count'] = Livre.objects.filter(disponible=False).count()
        return ctx


class LivreCreateView(CreateView):
    model = Livre
    template_name = 'core/livre_form.html'
    fields = ['titre', 'auteur', 'isbn', 'date_publication', 'prix', 'disponible']
    success_url = reverse_lazy('livre-list')


class LivreUpdateView(UpdateView):
    model = Livre
    template_name = 'core/livre_form.html'
    fields = ['titre', 'auteur', 'isbn', 'date_publication', 'prix', 'disponible']
    success_url = reverse_lazy('livre-list')


class LivreDeleteView(DeleteView):
    model = Livre
    template_name = 'core/livre_confirm_delete.html'
    success_url = reverse_lazy('livre-list')
