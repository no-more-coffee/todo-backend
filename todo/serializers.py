from rest_framework import serializers

from todo.models import Todo, Tag


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'url',
            'name',
            'is_done',
            'tags',
            'created',
            'modified',
        ]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'name']
