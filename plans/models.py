from django.db import models

# Create your models here.

class Plan_Category(models.Model):

    class Meta:
        verbose_name_plural = 'Plan_Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name 

class Plan(models.Model):
    plan_category = models.ForeignKey('plan_category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    plan_length = models.CharField(max_length=50)
    difficulty = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    days_per_week = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    description = models.TextField()
    equipment_needed = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name