from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LivreViewSet,
    LivreListView,
    LivreCreateView,
    LivreUpdateView,
    LivreDeleteView,
)

# basename='api-livre' évite le conflit de nom avec les vues web :
# le router génèrerait sinon 'livre-list' qui écrase notre URL web du même nom.
router = DefaultRouter()
router.register(r'livres', LivreViewSet, basename='api-livre')

urlpatterns = [
    # ── Interface web ────────────────────────────────────────────────────────
    path('', LivreListView.as_view(), name='livre-list'),
    path('ajouter/', LivreCreateView.as_view(), name='livre-create'),
    path('modifier/<int:pk>/', LivreUpdateView.as_view(), name='livre-update'),
    path('supprimer/<int:pk>/', LivreDeleteView.as_view(), name='livre-delete'),
] + router.urls
