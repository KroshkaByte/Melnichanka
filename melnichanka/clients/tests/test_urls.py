from django.urls import resolve
from clients.views import ClientsViewSet


def test__url_resolves_to_correct_view():
    match = resolve("/api/v1/clients/")
    assert match.func.__name__ == ClientsViewSet.as_view({"get": "list"}).__name__
