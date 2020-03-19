from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view

import todo.urls
import user.urls

schema_view = get_schema_view(
    title='Server Monitoring API',
    url='https://www.example.org/api/',
    renderer_classes=[JSONOpenAPIRenderer]
)

router = routers.DefaultRouter()
router.registry.extend(user.urls.router.registry)
router.registry.extend(todo.urls.router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('schema.json', schema_view),
    path('api/', include(router.urls)),
]
