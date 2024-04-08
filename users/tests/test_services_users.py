import pytest
from users.services import UserRelatedView
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate


@pytest.mark.django_db
def test__user_related_view__get_object_valid(user_object):
    view = UserRelatedView()
    request = APIRequestFactory().get("/fake-url/")
    request.user = user_object
    force_authenticate(request, user=user_object)
    view.request = request
    assert view.get_object() == user_object
