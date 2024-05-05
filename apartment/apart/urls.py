from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('residents', views.ResidentViewSet)
router.register('flats', views.FlatViewSet)
router.register('bills', views.BillViewSet)
router.register('items', views.ItemViewSet)
router.register('feedbacks', views.FeedbackViewSet)
router.register('surveys', views.SurveyViewSet)
router.register('famembers', views.FaMemberViewSet)

#/courses/ - GET
#/courses/ - POST
#/courses/{course_id} - GET
#/courses/{course_id} - PUT
#/courses/{course_id} - DELETE

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls),
]