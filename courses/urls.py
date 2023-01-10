from rest_framework.routers import SimpleRouter

from .views import CourseAPIViewSet

router = SimpleRouter()
router.register("", CourseAPIViewSet, basename="course")

urlpatterns = router.urls
