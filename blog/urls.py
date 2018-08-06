from django.urls import path#,include,re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('index/', views.index),
    path('article/<int:article_id>/',views.article_page,name='article_page'),
    # re_path('article/(?P<article_id>[0-9]+)',views.article_page, name= 'article_id'),
    path('edit/<int:article_id>/', views.edit_page,name='edit_page'),
    path('edit/action/',views.edit_action,name='edit_action'),
    path('del/action/<int:article_id>/',views.del_action,name='del_action'),
    path('comment/action/<int:article_id>/',views.com_action,name='com_action'),
]
