from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # v1
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("products/", include("products.urls", namespace="products")),
                path("auth/", include("authtokens.urls", namespace="authtokens")),
                path("users/", include("users.urls", namespace="users")),
                path("search/", include("search.urls", namespace="search")),
            ]
        ),
    ),
]
