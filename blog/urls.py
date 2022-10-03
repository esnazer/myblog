from django.urls import path
from blog.views import ArticuloView

urlpatterns = [
    path('articulo/<id>/', ArticuloView.as_view(), name='articulo-blog')
]