from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=1024)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('todo.Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.name[:64]}'


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
