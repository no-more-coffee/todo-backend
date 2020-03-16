from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=1024)
    is_done = models.BooleanField(default=False)
    tags = models.ForeignKey(
        'todo.Tag',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=64)
