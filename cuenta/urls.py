from django.urls import path 
from django.shortcuts import redirect
from cuenta.views import Login, Logout, DashBoardView, ArticlesView, CategoriesView, Myadmin
from cuenta.views import AddArticlesView, EditArticlesView, DelArticlesView
from cuenta.views import AddCategoriesView, EditCategoriesView, DelCategoriesView

urlpatterns = [
    path('login/', Login.as_view(),name="login"),
    path('logout/', Logout.as_view(),name="logout"),
    path('admin/', Myadmin.as_view(),name="myadmin"),
    path('admin/dashboard/', DashBoardView.as_view(),name="dashboard"),
    path('admin/articles/', ArticlesView.as_view(),name="admin-articles-list"),
    path('admin/articles/add/', AddArticlesView.as_view(),name="admin-articles-add"),
    path('admin/articles/edit/<int:articl>/', EditArticlesView.as_view(),name="admin-articles-edit"),
    path('admin/articles/delete/', DelArticlesView.as_view(),name="admin-articles-delete"),
    path('admin/categories/', CategoriesView.as_view(),name="admin-categories-list"),
    path('admin/categories/add/', AddCategoriesView.as_view(),name="admin-categories-add"),
    path('admin/categories/edit/<int:catgri>/', EditCategoriesView.as_view(),name="admin-categories-edit"),
    path('admin/categories/delete/', DelCategoriesView.as_view(),name="admin-categories-delete"),
]