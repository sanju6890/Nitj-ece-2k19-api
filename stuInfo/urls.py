from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from .views import get_all_info, get_one_info, post_info, patch_info, delete_info
from .views import StudentViewSet

router = DefaultRouter()
router.register('api', StudentViewSet)

urlpatterns = [
    # path('', get_all_info),
    # path('get-one-info/<roll_no>/', get_one_info),
    # path('post-info/', post_info),
    # path('patch-info/<id>/', patch_info),
    # path('delete-info/<id>/', delete_info),   
    path('', include(router.urls)),
]