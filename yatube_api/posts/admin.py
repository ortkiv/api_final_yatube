from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'pub_date',
        'author',
        'group'
    )
    list_editable = ('group', 'text')
    search_fields = ('text',)
    list_filter = ('pub_date', 'group')
    empty_value_display = '-пусто-'


@admin.register(Group)
class PostGroup(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'description'
    )
    list_editable = ('title', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class PostFollow(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'following'
    )
    list_editable = ('user', 'following')


@admin.register(Comment)
class PostComment(admin.ModelAdmin):
    list_display = (
        'author',
        'post',
        'text',
        'created'
    )
    list_editable = ('text',)
