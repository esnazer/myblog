from django.shortcuts import render
from django.views import View
from blog.models import Articulo, Categoria

# Create your views here.
class BlogView(View):
    
    def get(self, request, **kwargs):
        articles = Articulo.objects.all()
        category = Categoria.objects.all()
        parmts = {}
        return render(request, 'blog/indice.html', parmts)


class ArticuloView(View):
    
    def get(self, request, **kwargs):
        id = kwargs['id']
        article = Articulo.objects.filter(pk=id).first()
        parmts = {
            'art_title': article.title,
            'art_description': article.description,
            'alert': ''
        }
        return render(request, 'blog/articulo.html', parmts)

class CategoriasView(View):
    def get(self, request, **kwargs):
        categorys = Categoria.objects.all()
        parmts = {
            'catgs': categorys
        }
        return render(request, 'blog/categorias.html', parmts)

class CategoriaView(View):
    def get(self, request, **kwargs):
        sel_catg = kwargs['categoria']
        articles = Articulo.objects.filter(categorias__slug=sel_catg)
        parmts = {
            'catg': kwargs['categoria'],
            'articles': articles
        }
        return render(request, 'blog/categoria.html', parmts)