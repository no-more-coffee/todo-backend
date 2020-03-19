from rest_framework import routers

from todo import views

router = routers.SimpleRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'tags', views.TagViewSet)
