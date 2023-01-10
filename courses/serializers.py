from rest_framework import serializers

from .models import Course


class CourseListSerializer(serializers.ModelSerializer):
    """Return short course information for collection of courses"""
    class Meta:
        model = Course
        fields = (
            "title",
            "rating"
            "price",
        )

    @staticmethod
    def get_number_of_courses(obj):
        return obj.courses.all().count()


class CourseDetailSerializer(serializers.ModelSerializer):
    """Return detail information for single course."""
    class Meta:
        model = Course
        fields = (
            "title",
            "overview",
            "price",
            "rating"
        )