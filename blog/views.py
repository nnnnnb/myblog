from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})

def article_page(request, article_id):
  #  if str(article_id) != '0':
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request,article_id):
    if str(article_id) == '0':
      return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article': article})

def edit_action(request):


    title = request.POST.get('title','TITLE')
    content = request.POST.get('content', 'CONTENT')#获取表单数据
    article_id = request.POST.get('article_id','0')

    if article_id == '0':
        models.Article.objects.create(title=title,content=content)#创建对象
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html',{'articles': articles})
        # return HttpResponseRedirect('/blog/index')
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title=title
        article.content=content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})

def del_action(request,article_id):
     models.Article.objects.filter(nid=article_id).delete()
     return HttpResponseRedirect("/blog/index.html")

