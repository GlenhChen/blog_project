# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *


# Register your models here.
# 给User自定义一个管理类，继承ModelAdmin
class UserAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'qq',)
    list_display_links = ('mobile',)

    fieldsets = (
        (None, {
            'fields': ('avatar', 'mobile', 'qq',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc',)

    fieldsets = (
       (None, {
           'fields': ('title', 'desc', 'content', 'user', 'category', 'tag')
       }),
       ('高级设置', {
           'classes': ('collapse',),
           'fields': ('click_count', 'is_recommend', )
       })
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


class TagAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


class CategoryAdmin(admin.ModelAdmin):

    fieldsets = (
       (None, {
           'fields': ('name', 'index',)
       }),
       )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'article',)
    list_display_links = ('user', 'article',)

    fieldsets = (
       (None, {
           'fields': ('content', 'user', 'article',)
       }),
       ('高级设置', {
           'classes': ('collapse',),
           'fields': ('pid', )
       })
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    list_display_links = ('title', 'description',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'callback_url', 'date_publish',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('index',)
        })
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_display_links = ('title', 'description',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image_url', 'callback_url ',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('date_publish', 'index',)
        })
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.4/kindeditor-min.js',
            '/static/js/kindeditor-4.1.4/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.4/config.js',
        )


admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Ad, AdAdmin)
