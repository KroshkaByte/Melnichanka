from django.test import RequestFactory
import pytest
from users.views import DepartmentListView, PositionListView
from users.models import CustomUser, Department, Position


@pytest.mark.django_db
def test__positionlist__list_object_valid(position_object):
    factory = RequestFactory()
    request = factory.get("/")

    view = PositionListView().as_view()
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test__departmentlist__list_object_valid(department_object):
    factory = RequestFactory()
    request = factory.get("/")

    view = DepartmentListView().as_view()
    response = view(request)

    assert response.status_code == 200
