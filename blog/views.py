# -*- coding:utf-8 -*-
import logging
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.conf import settings
# from django.core.paginator import Paginator, InvalidPage, EmptyPage,PageNotAnInteger
from django.db.models import Count
from models import *
from forms import *


logger = logging.getLogger('blog.views')


# Create your views here.
def global_setting(request):
    # 站点基本信息
    SITE_NAME=settings.SITE_NAME
    SITE_DESC=settings.SITE_DESC
    WEIBO_SINA=settings.PRO_EMAIL
    PRO_EMAIL=settings.PRO_EMAIL
    # 分类信息获取（导航）
    category_list = Category.objects.all()[:1]
    # 评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment')
    article_comment_list = [Article.objects.get(pk=comment['article'])for comment in comment_count_list]
    return locals()


def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到相应的网页'})
    except Exception as e:
        print(e)
    return render(request, 'article.html', locals())


def index(request):
    try:

        # 最新文章数据
        article_list = Article.objects.all()
        # paginator = getPage(request, article_list)

        # 文章归档
        # 1、先要去获取到文章中有的 年份-月份
        archive_list = Article.objects.distinct_date()
    except Exception as e:
        logger.error(e)
        # locals() 函数会以字典类型返回当前位置的全部局部变量。
    return render(request, 'index.html', locals())


# 注册
def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_date["username"],
                                           email=reg_form.cleaned_date["email"],
                                           url=reg_form.cleaned_date["url"],
                                           password=make_password(reg_form.cleaned_date["password"]),)
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backend.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'reg_html', locals())


# 登录
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_date["username"]
                password = login_form.cleaned_date["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败！'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason':'login_form.errors'})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'login.html', locals())


# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])


# 分页代码
# def getPage(request, article_list):
#     paginator = Paginator(article_list, 6)
#     try:
#         # 获取当前页，如果什么都没有就默认返回1
#         page = int(request.GET.get('page', 1))
#         article_list = paginator.page(page)
#     except (InvalidPage, EmptyPage, PageNotAnInteger):
#         article_list = paginator.page(1)
#     return article_list

