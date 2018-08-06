from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')#文章标题
    content = models.TextField(null=False, default='Content')#文章内容
    pub_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)#发表时间

    def __str__(self):
        return self.title


class Comment(models.Model):
    belong_article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论所属文章')#评论所属文章
    words = models.TextField(max_length=200, null=False)#评论内容
    time = models.DateTimeField(null=False, auto_now_add=True)#评论时间
    belong_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')#评论所属用户

    def __str__(self):
        return self.belong_user.username + '：' + self.words     #返回用户名及内容