from rest_framework.routers import DefaultRouter # type: ignore
from values_principles.views import ValueViewSet, PrincipleViewSet


router = DefaultRouter()
router.register(r'values', ValueViewSet, basename='value-list')
router.register(r'principles', PrincipleViewSet)

urlpatterns = router.urls