from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Course
from .serializers import *


class CourseAPIViewSet(ReadOnlyModelViewSet):
    """Return detail information about course and list of courses."""

    queryset = Course.objects.order_by("rating", "title").prefetch_related(
        "title", "rating", "price"
    ).all()

    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer

        return CourseDetailSerializer