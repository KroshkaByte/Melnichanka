import pytest
from rest_framework.test import APIClient

from users.serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PositionSerializer,
    UserUpdatePasswordSerializer,
)


@pytest.mark.django_db
def test__position_serializer__create_object_valid(position_object):
    assert PositionSerializer(position_object).data == {
        "id": position_object.id,
        "position": position_object.position,
    }


@pytest.mark.django_db
def test__position_serializer__get_object_valid(position_object):
    retrieved_position = PositionSerializer(position_object).data
    assert retrieved_position == {
        "id": position_object.id,
        "position": position_object.position,
    }


@pytest.mark.django_db
def test__department_serializer__create_object_valid(department_object):
    assert DepartmentSerializer(department_object).data == {
        "id": department_object.id,
        "department": department_object.department,
    }


@pytest.mark.django_db
def test__department_serializer__get_object_valid(department_object):
    retrieved_department = DepartmentSerializer(department_object).data
    assert retrieved_department == {
        "id": department_object.id,
        "department": department_object.department,
    }


@pytest.mark.django_db
def test__custom_user_serializer__create_object_valid(
    user_object, position_object, department_object
):
    serializer_data = CustomUserSerializer(user_object).data
    assert serializer_data["id"] == user_object.id
    assert serializer_data["email"] == user_object.email
    assert serializer_data["full_name"] == user_object.full_name
    assert serializer_data["position"] == position_object.id
    assert serializer_data["department"] == department_object.id
    assert serializer_data["phone_number_work"] == user_object.phone_number_work
    assert serializer_data["phone_number_personal"] == user_object.phone_number_personal


@pytest.mark.django_db
def test__custom_user_serializer__create_new_user(user_object, position_object, department_object):
    data = {
        "email": "testuser2@test.com",
        "full_name": "Test User 2",
        "position": position_object.id,
        "department": department_object.id,
        "phone_number_work": "+79998877663",
        "phone_number_personal": "+79998877664",
        "password": "testpass2",
        "password_confirm": "testpass2",
    }
    serializer = CustomUserSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert user.email == data["email"]
    assert user.full_name == data["full_name"]
    assert user.position.id == data["position"]
    assert user.department.id == data["department"]
    assert user.phone_number_work == data["phone_number_work"]
    assert user.phone_number_personal == data["phone_number_personal"]
    assert user.check_password(data["password"])


@pytest.mark.django_db
def test__custom_user_update_serializer__update_object_valid(
    user_object, position_object, department_object
):
    serializer_data = CustomUserSerializer(user_object).data
    assert serializer_data["id"] == user_object.id
    assert serializer_data["email"] == user_object.email
    assert serializer_data["full_name"] == user_object.full_name
    assert serializer_data["position"] == position_object.id
    assert serializer_data["department"] == department_object.id
    assert serializer_data["phone_number_work"] == user_object.phone_number_work
    assert serializer_data["phone_number_personal"] == user_object.phone_number_personal


@pytest.mark.django_db
def test__custom_user_serializer__password_too_short(
    user_object, position_object, department_object
):
    data = {
        "email": "testuser2@test.com",
        "full_name": "Test User 2",
        "position": position_object.id,
        "department": department_object.id,
        "phone_number_work": "+79998877663",
        "phone_number_personal": "+79998877664",
        "password": "short",
        "password_confirm": "short",
    }
    serializer = CustomUserSerializer(data=data)
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__custom_user_serializer__password_no_letters(
    user_object, position_object, department_object
):
    data = {
        "email": "testuser2@test.com",
        "full_name": "Test User 2",
        "position": position_object.id,
        "department": department_object.id,
        "phone_number_work": "+79998877663",
        "phone_number_personal": "+79998877664",
        "password": "12345678",
        "password_confirm": "12345678",
    }
    serializer = CustomUserSerializer(data=data)
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__custom_user_serializer__password_no_digits(
    user_object, position_object, department_object
):
    data = {
        "email": "testuser2@test.com",
        "full_name": "Test User 2",
        "position": position_object.id,
        "department": department_object.id,
        "phone_number_work": "+79998877663",
        "phone_number_personal": "+79998877664",
        "password": "abcdefgh",
        "password_confirm": "abcdefgh",
    }
    serializer = CustomUserSerializer(data=data)
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__custom_user_serializer__passwords_do_not_match(
    user_object, position_object, department_object
):
    data = {
        "email": "testuser2@test.com",
        "full_name": "Test User 2",
        "position": position_object.id,
        "department": department_object.id,
        "phone_number_work": "+79998877663",
        "phone_number_personal": "+79998877664",
        "password": "12345678",
        "password_confirm": "87654321",
    }
    serializer = CustomUserSerializer(data=data)
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__update_password_serializer__update_object_valid(user_object, rf):
    client = APIClient()
    client.force_authenticate(user=user_object)
    data = {
        "old_password": "testpass",
        "new_password": "testpass123",
        "new_password_confirm": "testpass123",
    }
    request = rf.get("/fake-url/")
    request.user = user_object
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["old_password"] == data["old_password"]
    assert serializer.validated_data["new_password"] == data["new_password"]
    assert serializer.validated_data["new_password_confirm"] == data["new_password_confirm"]


@pytest.mark.django_db
def test__user_update_password_serializer__old_password_incorrect(user_object, rf):
    client = APIClient()
    client.force_authenticate(user=user_object)
    data = {
        "old_password": "wrongpass",
        "new_password": "newpass123",
        "new_password_confirm": "newpass123",
    }
    request = rf.get("/fake-url/")
    request.user = user_object
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors
    assert serializer.errors["non_field_errors"][0] == "Старый пароль неверный"


@pytest.mark.django_db
def test__user_update_password_serializer__new_password_too_short(user_object, rf):
    client = APIClient()
    client.force_authenticate(user=user_object)
    data = {
        "old_password": "testpass",
        "new_password": "short",
        "new_password_confirm": "short",
    }
    request = rf.get("/fake-url/")
    request.user = user_object
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__user_update_password_serializer__new_password_no_letters(user_object, rf):
    client = APIClient()
    client.force_authenticate(user=user_object)
    data = {
        "old_password": "testpass",
        "new_password": "12345678",
        "new_password_confirm": "12345678",
    }
    request = rf.get("/fake-url/")
    request.user = user_object
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__user_update_password_serializer__new_password_no_digits(user_object, rf):
    client = APIClient()
    client.force_authenticate(user=user_object)
    data = {
        "old_password": "testpass",
        "new_password": "abcdefgh",
        "new_password_confirm": "abcdefgh",
    }
    request = rf.get("/fake-url/")
    request.user = user_object
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors


@pytest.mark.django_db
def test__user_update_password_serializer__new_passwords_do_not_match(user_object, rf):
    client = APIClient()
    client.force_authenticate(user=user_object)
    data = {
        "old_password": "testpass",
        "new_password": "12345678",
        "new_password_confirm": "87654321",
    }
    request = rf.get("/fake-url/")
    request.user = user_object
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors
