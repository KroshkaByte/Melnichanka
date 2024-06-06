from django.urls import include, path
from rest_framework import routers

from .views import GoodsViewSet, FactoryListAPIView

router = routers.SimpleRouter()
router.register(r"goods", GoodsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("factories/", FactoryListAPIView.as_view(), name="factory-list")
]
