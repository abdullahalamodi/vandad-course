from django.urls import path
from .views import MakerListView, ProductCategoryListView, ProductListView


app_name = "products"

urlpatterns = [
    path("categories", ProductCategoryListView.as_view(), name="categories-list"),
    path("makers", MakerListView.as_view(), name="makers-list"),
    path("", ProductListView.as_view(), name="products-list"),
]
