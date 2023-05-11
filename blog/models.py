from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255,blank=True)


# Sample Product Model with Foreign Key Relations
# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     release_date = models.DateField()
#     last_updated = models.DateTimeField(auto_now=True)
#     opening_time = models.TimeField()
#     stock_count = models.IntegerField()
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)
#     tags = models.ManyToManyField('Tag')

# class Category(models.Model):
#     name = models.CharField(max_length=255)

# class Tag(models.Model):
#     name = models.CharField(max_length=255)
