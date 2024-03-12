import pytest
from users.models import CustomUser, Department, Position


@pytest.mark.django_db
def test__position__create_object_valid(position_object):
    assert position_object.position == "position"


@pytest.mark.django_db
def test__position__get_object_valid(position_object):
    retrieved_position = Position.objects.get(id=position_object.id)
    assert retrieved_position.position == position_object.position


@pytest.mark.django_db
def test__position__return_valid_str(position_object):
    assert str(position_object) == "position"


@pytest.mark.django_db
def test__department__create_object_valid(department_object):
    assert department_object.department == "department"


@pytest.mark.django_db
def test__department__get_object_valid(department_object):
    retrieved_department = Department.objects.get(id=department_object.id)
    assert retrieved_department.department == department_object.department


@pytest.mark.django_db
def test__department__return_valid_str(department_object):
    assert str(department_object) == "department"
