import pytest
from users.models import CustomUser, Department, Position


@pytest.fixture
def position_object():
    return Position.objects.create(id=100, position="position")


@pytest.fixture
def department_object():
    return Department.objects.create(id=100, department="department")


@pytest.fixture
def user_object(position_object, department_object):
    user = CustomUser.objects.create(
        id=100,
        email="testuser@test.com",
        full_name="Test User",
        position=position_object,
        department=department_object,
        phone_number_work="+79998877662",
        phone_number_personal="+79998877661",
    )
    user.set_password("testpass")
    user.save()
    return user


@pytest.fixture
def customusermanager_object():
    return CustomUser.objects.create_user(
        id=101,
        email="testuser1@test.com",
        full_name="Test User 11",
        password="testpass1",
    )


@pytest.fixture
def customsuperusermanager_object():
    return CustomUser.objects.create_superuser(
        id=102,
        email="testuser2@test.com",
        full_name="Test User 22",
        password="testpass2",
        is_superuser=True,
    )
