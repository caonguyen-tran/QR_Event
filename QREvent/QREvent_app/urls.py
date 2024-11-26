from django.urls import path, include
from .admin import admin_site
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls),
]