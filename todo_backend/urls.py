from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import todo.urls
import user.urls

router = routers.DefaultRouter()
router.registry.extend(user.urls.router.registry)
router.registry.extend(todo.urls.router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
