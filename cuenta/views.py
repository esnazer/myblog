from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.db.models import Sum, Avg
from django.http import HttpResponse
from django.views import View
from blog.models import Categoria, Articulo
from cuenta.forms import ArticlesForm, CategoryForm
from django.contrib import messages


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
        articulos = Articulo.objects.all()
        parmts = {
            'articulos' : articulos
        }
        return render(request, 'adminblog/article.html', parmts)
    
class AddArticlesView(View):
    def get(self, request):
        form = ArticlesForm()
        parmts = {
            'form_new': form
        }
        return render(request, 'adminblog/article_new.html', parmts)
    def post(self, request):
        form = ArticlesForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = request.user
            usuario.save()
            form.save_m2m()
            return redirect(reverse('admin-articles-list'))
        else:
            parmts = {
                'form_new': form
            }
            return render(request, 'adminblog/article_new.html', parmts)

class EditArticlesView(View):
    def get(self, request, articl):
        artEdit = Articulo.objects.get(pk=articl)
        form = ArticlesForm(instance=artEdit)
        parmts = {
            'form_edit': form,
            'articulo': artEdit.id
        }
        return render(request, 'adminblog/article_edit.html', parmts)
    def post(self, request, articl):
        artEdit = Articulo.objects.get(pk=articl)
        form = ArticlesForm(request.POST, instance=artEdit)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = request.user
            usuario.save()
            form.save_m2m()
            print('formulario valido')
        parmts = {
            'form_edit': form,
            'articulo': artEdit.id
        }
        return render(request, 'adminblog/article_edit.html', parmts)

class DelArticlesView(View):
    def post(self, request):
        if 'del_art' in request.POST:
            articl = request.POST['del_art']
            artDel = Articulo.objects.get(pk=articl)
            artDel.delete()
        return redirect(reverse('admin-articles-list'))


class CategoriesView(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        parmts = {
            'categorias' : categorias
        }
        return render(request, 'adminblog/category.html', parmts)

class AddCategoriesView(View):
    def get(self, request):
        form = CategoryForm()
        parmts = {
            'form_new': form
        }
        return render(request,'adminblog/category_new.html', parmts)
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-categories-list'))
        else:
            parmts = {
                'form_new': form
            }
            return render(request,'adminblog/category_new.html', parmts)

class EditCategoriesView(View):
    def get(self, request, catgri):
        catgEdit = Categoria.objects.get(pk=catgri)
        form = CategoryForm(instance=catgEdit)
        parmts = {
            'categoria': catgEdit.id,
            'form_edit': form
        }
        return render(request,'adminblog/category_edit.html', parmts)
    def post(self, request, catgri):
        catgEdit = Categoria.objects.get(pk=catgri)
        form = CategoryForm(request.POST, instance=catgEdit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria guardada correctamente')
        parmts = {
            'categoria': catgEdit.id,
            'form_edit': form
        }
        return render(request,'adminblog/category_edit.html', parmts)

class DelCategoriesView(View):
    def post(self, request):
        if 'del_cat' in request.POST:
            catg = request.POST['del_cat']
            catgDel = Categoria.objects.get(pk=catg)
            catgDel.delete()
        return redirect(reverse('admin-categories-list'))