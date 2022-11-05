from django.urls import path 
from django.shortcuts import redirect
from cuenta.views import Login, Logout, DashBoardView, ArticlesView, CategoriesView, Myadmin
from cuenta.views import AddArticlesView

urlpatterns = [
    path('login/', Login.as_view(),name="login"),
    path('logout/', Logout.as_view(),name="logout"),
    path('admin/', Myadmin.as_view(),name="myadmin"),
    path('admin/dashboard/', DashBoardView.as_view(),name="dashboard"),
    path('admin/articles/', ArticlesView.as_view(),name="admin-articles-list"),
    path('admin/articles/add/', AddArticlesView.as_view(),name="admin-articles-add"),
    path('admin/articles/update/', ArticlesView.as_view(),name="admin-articles-update"),
    path('admin/articles/delete/', ArticlesView.as_view(),name="admin-articles-delete"),
    path('admin/categories/', CategoriesView.as_view(),name="admin-categories"),
]