import pytest
from users.serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PositionSerializer,
)


@pytest.mark.django_db
def test__positionserializer__create_object_valid(position_object):
    assert PositionSerializer(position_object).data == {
        "id": position_object.id,
        "position": "position",
    }


@pytest.mark.django_db
def test__positionserializer__get_object_valid(position_object):
    retrieved_position = PositionSerializer(position_object).data
    assert retrieved_position == {
        "id": position_object.id,
        "position": "position",
    }


@pytest.mark.django_db
def test__departmentserializer__create_object_valid(department_object):
    assert DepartmentSerializer(department_object).data == {
        "id": department_object.id,
        "department": "department",
    }


@pytest.mark.django_db
def test__departmentserializer__get_object_valid(department_object):
    retrieved_department = DepartmentSerializer(department_object).data
    assert retrieved_department == {
        "id": department_object.id,
        "department": "department",
    }
