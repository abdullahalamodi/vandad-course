from django.db import models
from django.db.models import Q


class ProductQuerySet(models.QuerySet):

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(subtitle__icontains=query)
        qs = self.filter(lookup)
        return qs


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model)

    def search(self, query):
        return self.get_queryset().search(query)
