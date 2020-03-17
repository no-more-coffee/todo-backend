from django.contrib import admin

from todo.models import Todo, Tag


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_done', 'created', 'modified')
    search_fields = ('id', 'name')
    list_filter = ('is_done', 'tags')
    fields = ('name', 'is_done', 'tags', 'created', 'modified')
    readonly_fields = ('created', 'modified')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

