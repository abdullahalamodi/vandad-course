from django.urls import path

from search.views import AlgoliaSearchListView, SearchListView


app_name = "search"

urlpatterns = [
    path("", SearchListView.as_view(), name="search"),
    path("algolia/", AlgoliaSearchListView.as_view(), name="algolia-search"),
]
