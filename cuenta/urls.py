from django.urls import path
from cuenta.views import login, logout

urlpatterns = [
    path('login/', login.as_view(),name="login"),
    path('logout/', login.as_view(),name="logout"),
]