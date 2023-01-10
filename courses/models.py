from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-rating', 'title']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ranked:company_list_by_rating', args=[self.slug])


class Course(models.Model):
    """Model for store courses with their base information in our service."""
    company = models.ForeignKey(Company,
                                related_name='courses',
                                on_delete=models.CASCADE)

    title = models.CharField(max_length=200, db_index=True)
    overview = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-rating', 'title']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ranked:course_list_by_rating', args=[self.slug])
