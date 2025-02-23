from urllib import request
from rest_framework import generics, permissions, authentication

from utils.mixins import (
    ResponseWrapperMixin,
    StaffEditorPermissionMixin,
    UserQuerysetMixin,
)
from .models import Maker, Product, ProductCategory
from .serializers import MakerSerializer, ProductCategorySerializer, ProductSerializer


class ProductCategoryListView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class MakerListView(generics.ListAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer


# products


class ProductListView(
    StaffEditorPermissionMixin,
    ResponseWrapperMixin,
    generics.ListAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailsView(
    # StaffEditorPermissionMixin,
    ResponseWrapperMixin,
    generics.RetrieveAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(
    StaffEditorPermissionMixin,
    generics.CreateAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
