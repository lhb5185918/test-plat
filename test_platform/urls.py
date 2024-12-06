from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import test_case_views

router = DefaultRouter()
router.register(r'testcases', test_case_views.TestCaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 