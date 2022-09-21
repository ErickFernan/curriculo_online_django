from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Se for na raiz mando pro index
]