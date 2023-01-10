from django.contrib import admin

from .models import Course, Company


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'overview', 'rating']
    list_filter = ['price', 'rating']
    list_editable = ['price', 'overview', 'rating']
    prepopulated_fields = {'slug': ('title',)}


class CourseInline(admin.StackedInline):
    model = Course


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']
    list_editable = ['rating']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CourseInline]
