import json

import pytest
from django.core.cache import cache
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test__data_doc_view__unauthorized_user_cannot_post_data(make_test_data):
    client = APIClient()
    url = reverse("data")
    response = client.post(url, make_test_data, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test__data_doc_view__authorized_user_can_post_data(authorized_client, make_test_data):
    url = reverse("data")
    response = authorized_client.post(url, make_test_data, format="json")
    assert response.status_code == 200


@pytest.mark.django_db
def test__data_doc_view__authorized_user_post_data_response_is_correct(authorized_client,
                                                                       make_test_data):
    url = reverse("data")
    response = authorized_client.post(url, make_test_data, format="json")
    assert response.status_code == 200
    assert response.json() == {"Success": True}


@pytest.mark.django_db
def test__create_docs_view__authorized_user_get_valid_data(authorized_client, make_test_data):
    url = reverse("file")
    cache_key = f"validated_data_{authorized_client.user.id}"
    cache.set(cache_key, json.dumps(make_test_data), timeout=120)
    response = authorized_client.get(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Documents saved"}
    cache.delete(cache_key)


@pytest.mark.django_db
def test__create_docs_view__authorized_user_get_no_data(authorized_client):
    url = reverse("file")
    response = authorized_client.get(url)
    assert response.status_code == 400
    assert response.json() == {"error": "No data found in cache"}


@pytest.mark.django_db
def test__download_doc_view__returns_404_when_no_file_exists(authorized_client):
    url = reverse("downloadfile")
    response = authorized_client.get(url)
    assert response.status_code == 404
    assert response.json() == {"error": "No file found"}
