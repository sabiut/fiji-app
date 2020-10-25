from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('login_user/', views.login_user, name ="login_user"),
    path('logout/', views.logout_view, name='logout'),
    path('invalid_page/', views.invalid_page, name="invalid_page")

]
