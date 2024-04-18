import pytest

from users.models import CustomUser, Department, Position


@pytest.fixture
def position_object(faker):
    return Position.objects.create(id=faker.pyint(), position=faker.pystr())


@pytest.fixture
def department_object(faker):
    return Department.objects.create(id=faker.pyint(), department=faker.pystr())


@pytest.fixture
def user_object(position_object, department_object, faker):
    user = CustomUser.objects.create(
        id=faker.pyint(),
        email=faker.email(),
        full_name=faker.pystr(),
        position=position_object,
        department=department_object,
        phone_number_work=faker.phone_number(),
        phone_number_personal=faker.phone_number(),
    )
    user.set_password("testpass")
    user.save()
    return user
