from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from blog.models import Categoria, Articulo

# Create your views here.
class Login(View):
    def get(self, request):
        parameters = {
            'form' : '',
        }
        return render(request, '', parameters)

    def post(self,request):
        parameters = {
            'form' : '',
        }
        return render(request, '', parameters)


class Logout(View):
    def get(self, request):
        parameters = {
            'form' : '',
        }
        return render(request, '', parameters)

class Myadmin(View):
    def get(self, request):
        parameters = {
            'form' : '',
        }
        return redirect('/admin/dashboard/')

class DashBoardView(View):
    def get(self, request):
        cnt_articulos = Articulo.objects.count()
        cnt_categorias = Categoria.objects.count()
        articulos = Articulo.objects.filter().values()
        print(articulos[0].get('update'))
        categorias = Categoria.objects.all()
        parmts = {
            'cnt_articulos': cnt_articulos,
            'cnt_categorias': cnt_categorias,
            'articulos': articulos,
            'categorias': categorias
        }
        return render(request, 'adminblog/dashboard.html', parmts)


class ArticlesView(View):
    def get(self, request):
        parmts = {}
        return render(request, '', parmts)

class CategoriesView(View):
    def get(self, request):
        parmts = {}
        return render(request, '', parmts)