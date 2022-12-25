from django.contrib import admin

from ranked.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'price', 'overview', 'rating']
    list_filter = ['title', 'price', 'rating']
    list_editable = ['title', 'price', 'overview', 'rating']
    prepopulated_fields = {'slug': ('title',)}