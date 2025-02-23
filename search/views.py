from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from search import client


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        result = Product.objects.none()
        if q is not None:
            result = qs.search(q)
        return result


class AlgoliaSearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        filters = request.GET.get("filters")
        if not query:
            return Response("", status=400)
        results = client.perform_search(
            query,
            filters=filters,
        )
        return Response(results)
