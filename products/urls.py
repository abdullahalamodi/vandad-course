from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path("categories", views.ProductCategoryListView.as_view(), name="categories-list"),
    path("makers", views.MakerListView.as_view(), name="makers-list"),
    path("", views.ProductListView.as_view(), name="products-list"),
    path("<int:pk>/", views.ProductDetailsView.as_view(), name="product-details"),
    path("create/", views.ProductCreateView.as_view(), name="product-create"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/delete/", views.ProductDestroyView.as_view(), name="product-delete"),
]
