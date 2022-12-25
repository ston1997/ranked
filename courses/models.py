from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    overview = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slag = models.SlugField(max_length=200, unique=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ('title',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ranked:course_list_by_rating', args=[self.slug])