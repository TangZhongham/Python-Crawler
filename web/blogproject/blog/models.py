from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    # 分类是一对多关系用foreignkey
    # 标签是多对多乱用，用ManytoMany
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # django.contrib.auth 内置应用专门用来处理网站用户注册登陆等流程，
    # django帮我们写好了然后因为是多对一的关系用ForeignKey
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']


