from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.contrib import auth
import json


from .models import Article
from .models import Comment
# 引入我们创建的表单类
from .forms import AddForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
        content = {}
        article1 = Article.objects.get(id=article_id)
        # 查询评论表，查询条件是评论所属id是article_id   #  跨文件获取id，在属性后面加上‘__’
        com = Comment.objects.filter(belong_article__id=article_id)
        print(com)
        #  获取article1信息
        content['article'] = article1
        content['com'] = com
        # 渲染blog/article_page.html页面，content传值
        return render(request, 'blog/article_page.html', content)


def edit_page(request,article_id):
    if str(article_id) == '0':
      return render(request,'blog/edit_page.html')
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


@csrf_exempt
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')#获取表单数据
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        Article.objects.create(title=title, content=content)#创建对象
        articles = Article.objects.all()
        return render(request, 'blog/index.html',{'articles': articles})
        # return HttpResponseRedirect('/blog/index')
    else:
        article = Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})


def del_action(request,article_id):
    # 删除符合条件的结果
     Article.objects.filter(id=article_id).delete()
     return HttpResponseRedirect("/blog/index/")


@csrf_exempt
def com_action(request,article_id):
    if request.method == "POST":# 当提交表单时
        form = AddForm(request.POST)# form 包含提交的数据
        if form.is_valid():#如果提交的数据合法
            comment = form.cleaned_data['cominput']
            article = Article.objects.get(id=article_id)   #获取文章信息
            uu = User.objects.all()[1]#获得第二个用户名
            c = Comment(belong_user=uu, words=comment, belong_article=article)   #获取评论所属的用户，内容，所属文章
            c.save()#保存
            return redirect('/blog/article/' + str(article_id))
    return redirect('/blog/article/' + str(article_id))