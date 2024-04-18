import pytest
from django.db import models
from django.db.models import ProtectedError
from phonenumber_field.modelfields import PhoneNumberField

from users.models import CustomUser


@pytest.mark.django_db
def test__position__return_valid_str(position_object):
    assert str(position_object) == position_object.position


@pytest.mark.django_db
def test__department__return_valid_str(department_object):
    assert str(department_object) == department_object.department


@pytest.mark.django_db
def test_customuser_fields():
    assert isinstance(CustomUser._meta.get_field("email"), models.EmailField)
    assert isinstance(CustomUser._meta.get_field("full_name"), models.CharField)
    assert isinstance(CustomUser._meta.get_field("position"), models.ForeignKey)
    assert isinstance(CustomUser._meta.get_field("department"), models.ForeignKey)
    assert isinstance(CustomUser._meta.get_field("phone_number_work"), PhoneNumberField)
    assert isinstance(CustomUser._meta.get_field("phone_number_personal"), PhoneNumberField)


@pytest.mark.django_db
def test__delete_position_and_department_with_related_users(
    position_object, department_object, user_object
):
    with pytest.raises(ProtectedError):
        department_object.delete()
        position_object.delete()


@pytest.mark.django_db
def test__custom_user__return_valid_str(user_object):
    assert str(user_object) == f"Пользователь {user_object.full_name} {user_object.email}"
