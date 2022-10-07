from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

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


class DashBoardView(View):
    def get(self, request):
        parmts = {}
        return render(request, '', parmts)


class ArticlesView(View):
    def get(self, request):
        parmts = {}
        return render(request, '', parmts)

class CategoriesView(View):
    def get(self, request):
        parmts = {}
        return render(request, '', parmts)