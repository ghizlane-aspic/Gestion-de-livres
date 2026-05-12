from django.urls import path

from .views import LivreListView, LivreCreateView, LivreUpdateView, LivreDeleteView

urlpatterns = [
    path('', LivreListView.as_view(), name='livre-list'),
    path('ajouter/', LivreCreateView.as_view(), name='livre-create'),
    path('modifier/<int:pk>/', LivreUpdateView.as_view(), name='livre-update'),
    path('supprimer/<int:pk>/', LivreDeleteView.as_view(), name='livre-delete'),
]
