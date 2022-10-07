from django.urls import path
from blog.views import ArticuloView, BlogView, CategoriasView, CategoriaView

urlpatterns = [
    path('', BlogView.as_view(), name='full-blog'),
    path('artcs/<id>/', ArticuloView.as_view(), name='articulo-blog'),
    path('catgs/', CategoriasView.as_view(), name='categorias-blog'),
    path('catgs/<categoria>/', CategoriaView.as_view(), name='articulos-categoria-blog'),
]