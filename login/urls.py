from django.urls import path#,include,re_path
from django.conf.urls import include
from . import views
from django.contrib import admin

app_name = 'login'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login_action),
    path('register/', views.register),
    path('logout/', views.logout),

   ]