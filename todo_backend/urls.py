from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import user.views
import todo.views

router = routers.DefaultRouter()
router.register(r'users', user.views.UserViewSet)
router.register(r'groups', user.views.GroupViewSet)
router.register(r'todos', todo.views.TodoViewSet)
router.register(r'tags', todo.views.TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
