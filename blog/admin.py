from ctypes.wintypes import POINT
from django.contrib import admin
from .models import Post, Tag, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostCommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ('__all__')    


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostCommentInline]
    form = PostAdminForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'post')
    list_display_links = ('owner',)
    search_fields = ('owner__username', 'post__title')
    prepopulated_fields = {'slug': ('owner', 'post')}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
