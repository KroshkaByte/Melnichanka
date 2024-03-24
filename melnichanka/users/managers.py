from django.contrib.auth.models import BaseUserManager
from django.db import IntegrityError, transaction
from django.utils.translation import gettext_lazy as _


# Менеджер пользователей
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        Создает  и сохраняет пользователя с указанным email, ФИО и другими полями
        """
        if not email:
            raise ValueError(_("Email должен быть указан"))
        try:
            with transaction.atomic():
                email = self.normalize_email(email)
                user = self.model(email=email, full_name=full_name, **extra_fields)
                user.set_password(password)
                user.save(using=self.db)
                return user
        except IntegrityError:
            raise ValueError("Пользователь с таким email уже существует")
        except (TypeError, ValueError):
            raise ValueError("Неправильные данные для создания пользователя")

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        """
        Создает  и сохраняет суперпользователя с указанным email, ФИО и другими полями
        Проверяет действительно ли суперпользователь является им
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, full_name, password=password, **extra_fields)
