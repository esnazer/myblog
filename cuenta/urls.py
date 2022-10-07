from django.urls import path 
from django.shortcuts import redirect
from cuenta.views import Login, Logout, DashBoardView, ArticlesView, CategoriesView

urlpatterns = [
    path('login/', Login.as_view(),name="login"),
    path('logout/', Logout.as_view(),name="logout"),
    path('admin/dashboard/', DashBoardView.as_view(),name="dashboard"),
    path('admin/articles/', ArticlesView.as_view(),name="admin-articles"),
    path('admin/categories/', CategoriesView.as_view(),name="admin-categories"),
]