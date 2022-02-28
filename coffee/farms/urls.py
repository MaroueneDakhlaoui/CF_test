from django.urls import path
from rest_framework import routers
from .api import FarmViewSet

router = routers.DefaultRouter()
router.register(r'farms', FarmViewSet, basename='farms')
urlpatterns = router.urls
