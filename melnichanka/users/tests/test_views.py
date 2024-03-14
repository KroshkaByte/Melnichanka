import pytest
from users.serializers import UserUpdatePasswordSerializer, UserUpdateSerializer
from users.views import (
    DepartmentListView,
    PositionListView,
    LoginView,
    LogoutView,
    UserCreateView,
    UserUpdateView,
    UserUpdatePasswordView,
)
from django.test import RequestFactory
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test__positionlist__list_object_valid(position_object):
    factory = RequestFactory()
    request = factory.get("/")

    view = PositionListView().as_view()
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test__department_list__list_object_valid(department_object):
    factory = RequestFactory()
    request = factory.get("/")

    view = DepartmentListView().as_view()
    response = view(request)

    assert response.status_code == 200
    for item in response.data:
        assert "department" in item


@pytest.mark.django_db
def test__login_user___valid(user_object):
    factory = RequestFactory()
    request = factory.post(
        "/api/v1/users/login/", {"email": "testuser@test.com", "password": "testpass"}
    )
    force_authenticate(request, user=user_object)
    view = LoginView().as_view()
    response = view(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test__logout_user___valid(user_object):
    refresh = RefreshToken.for_user(user_object)

    factory = RequestFactory()
    data = {"refresh_token": str(refresh)}
    request = factory.post("/api/v1/users/logout/", data)
    force_authenticate(request, user=user_object)
    view = LogoutView().as_view()
    response = view(request)
    assert response.status_code == 205


@pytest.mark.django_db
def test__create_user___valid(user_object, position_object, department_object):
    factory = RequestFactory()
    request = factory.post(
        "/api/v1/users/registration/",
        {
            "email": "testuser31@test.com",
            "full_name": "Test User 3",
            "position": position_object.id,
            "department": department_object.id,
            "phone_number_work": "+79998877665",
            "phone_number_personal": "+79998877666",
            "password": "testpass3",
            "password_confirm": "testpass3",
        },
    )
    view = UserCreateView().as_view()
    response = view(request)
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_update_view(user_object, rf):
    view = UserUpdateView()
    request = rf.put("/fake-url/")
    request.user = user_object
    force_authenticate(request, user=user_object)
    data = {
        "email": "updateduser@test.com",
        "full_name": "Updated User",
        "position": user_object.position.id,
        "department": user_object.department.id,
        "phone_number_work": "+79998877665",
        "phone_number_personal": "+79998877666",
    }
    serializer = UserUpdateSerializer(data=data, context={"request": request})
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["email"] == data["email"]
    assert serializer.validated_data["full_name"] == data["full_name"]
    assert serializer.validated_data["position"].id == data["position"]
    assert serializer.validated_data["department"].id == data["department"]
    assert serializer.validated_data["phone_number_work"] == data["phone_number_work"]
    assert (
        serializer.validated_data["phone_number_personal"]
        == data["phone_number_personal"]
    )


@pytest.mark.django_db
def test_user_update_password_view(user_object, rf):
    view = UserUpdatePasswordView()
    request = rf.put("/fake-url/")
    request.user = user_object
    force_authenticate(request, user=user_object)
    data = {
        "old_password": "testpass",
        "new_password": "testpass123",
        "new_password_confirm": "testpass123",
    }
    serializer = UserUpdatePasswordSerializer(data=data, context={"request": request})
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["old_password"] == data["old_password"]
    assert serializer.validated_data["new_password"] == data["new_password"]
    assert (
        serializer.validated_data["new_password_confirm"]
        == data["new_password_confirm"]
    )
