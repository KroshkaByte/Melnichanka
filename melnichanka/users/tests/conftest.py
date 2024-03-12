import pytest
from users.models import CustomUser, Department, Position


@pytest.fixture
def position_object():
    return Position.objects.create(id=100, position="position")


@pytest.fixture
def department_object():
    return Department.objects.create(id=100, department="department")
