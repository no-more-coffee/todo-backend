from django.contrib import admin

from todo.models import Todo, Tag


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_done', 'created', 'modified', 'get_tags')
    list_filter = ('is_done', 'tags')
    search_fields = ('id', 'name')
    fields = ('name', 'is_done', 'tags', 'created', 'modified')
    filter_horizontal = ('tags',)
    readonly_fields = ('created', 'modified')

    def get_tags(self, instance: Todo):
        return ';'.join(instance.tags.values_list('name', flat=True))
    get_tags.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
