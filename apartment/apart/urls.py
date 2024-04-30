from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flats', views.FlatViewSet)

#/courses/ - GET
#/courses/ - POST
#/courses/{course_id} - GET
#/courses/{course_id} - PUT
#/courses/{course_id} - DELETE
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls)
]