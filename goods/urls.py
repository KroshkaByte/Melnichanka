from django.urls import include, path
from rest_framework import routers

from .views import GoodsViewSet

router = routers.SimpleRouter()
router.register(r"", GoodsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
