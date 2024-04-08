from django.urls import resolve
from clients.views import ClientsAPIView, ClientAPIUpdateView, ClientAPIDeleteView


def test__clients__url_resolves_to_correct_view():
    match = resolve("/api/v1/clients/")
    assert match.func.__name__ == ClientsAPIView.as_view().__name__


def test__clients_update__url_resolves_to_correct_view():
    match = resolve("/api/v1/clients/10/")
    assert match.func.__name__ == ClientAPIUpdateView.as_view().__name__


def test__clients_delete__url_resolves_to_correct_view():
    match = resolve("/api/v1/clients/delete/10/")
    assert match.func.__name__ == ClientAPIDeleteView.as_view().__name__
