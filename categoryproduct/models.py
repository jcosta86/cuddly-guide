from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    id_channel = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
