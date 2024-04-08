import pytest
from django.db import models
from django.db.models import ProtectedError
from phonenumber_field.modelfields import PhoneNumberField
from users.models import CustomUser, Department, Position


@pytest.mark.django_db
def test__position__return_valid_str(position_object):
    assert str(position_object) == "position"


@pytest.mark.django_db
def test__department__return_valid_str(department_object):
    assert str(department_object) == "department"


@pytest.mark.django_db
def test_customuser_fields():
    assert isinstance(CustomUser._meta.get_field("email"), models.EmailField)
    assert isinstance(CustomUser._meta.get_field("full_name"), models.CharField)
    assert isinstance(CustomUser._meta.get_field("position"), models.ForeignKey)
    assert isinstance(CustomUser._meta.get_field("department"), models.ForeignKey)
    assert isinstance(CustomUser._meta.get_field("phone_number_work"), PhoneNumberField)
    assert isinstance(CustomUser._meta.get_field("phone_number_personal"), PhoneNumberField)


@pytest.mark.django_db
def test__create_user_with_invalid_email():
    with pytest.raises(ValueError):
        CustomUser.objects.create_user(
            email=None,
            full_name="Test User",
            password="testpass",
        )


@pytest.mark.django_db
def test__delete_position_and_department_with_related_users():
    position = Position.objects.create(id=120, position="position")
    department = Department.objects.create(id=120, department="department")
    user = CustomUser.objects.create_user(
        id=121,
        email="testuser121@test.com",
        full_name="Test User",
        password="testpass",
        position=position,
    )
    with pytest.raises(ProtectedError):
        department.delete()
        position.delete()


@pytest.mark.django_db
def test__custom_user__create_object_valid(user_object, position_object, department_object):
    assert user_object.email == "testuser@test.com"
    assert user_object.full_name == "Test User"
    assert user_object.position == position_object
    assert user_object.department == department_object
    assert user_object.phone_number_work == "+79998877662"
    assert user_object.phone_number_personal == "+79998877661"


@pytest.mark.django_db
def test__custom_user__get_object_valid(user_object):
    retrieved_user = CustomUser.objects.get(id=user_object.id)
    assert retrieved_user.email == user_object.email
    assert retrieved_user.full_name == user_object.full_name
    assert retrieved_user.position == user_object.position
    assert retrieved_user.department == user_object.department
    assert retrieved_user.phone_number_work == user_object.phone_number_work
    assert retrieved_user.phone_number_personal == user_object.phone_number_personal


@pytest.mark.django_db
def test__custom_user__return_valid_str(user_object):
    assert str(user_object) == f"Пользователь {user_object.full_name} {user_object.email}"


@pytest.mark.django_db
def test__custom_user_manager__create_object_valid(customusermanager_object):
    assert customusermanager_object.email == "testuser1@test.com"
    assert customusermanager_object.full_name == "Test User 11"
    assert customusermanager_object.check_password("testpass1")


@pytest.mark.django_db
def test__custom_user_manager__get_object_valid(customusermanager_object):
    assert customusermanager_object.email == "testuser1@test.com"
    assert customusermanager_object.full_name == "Test User 11"
    assert customusermanager_object.check_password("testpass1")


@pytest.mark.django_db
def test__custom_user_manager__email_is_unique(customusermanager_object):
    with pytest.raises(ValueError):
        CustomUser.objects.create_user(
            id=103,
            email="testuser1@test.com",
            full_name="Test User",
            password="testpass",
        )


@pytest.mark.django_db
def test__custom_user_manager__create_superuser_object_valid(
    customsuperusermanager_object,
):
    assert customsuperusermanager_object.email == "testuser2@test.com"
    assert customsuperusermanager_object.full_name == "Test User 22"
    assert customsuperusermanager_object.is_superuser
    assert customsuperusermanager_object.check_password("testpass2")
