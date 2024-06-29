from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import IntegrityError, models, transaction
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Position(models.Model):
    """
    A model for storing information about user positions.
    """

    position = models.CharField(max_length=30, verbose_name="Название позиции")

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

    def __str__(self) -> str:
        return self.position


class Department(models.Model):
    """
    A model for storing information about user departments.
    """

    department = models.CharField(max_length=50, verbose_name="Название департамента")

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self) -> str:
        return self.department


class CustomUserManager(BaseUserManager["CustomUser"]):
    """
    Custom user manager implementing user and superuser creation.
    """

    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and full name.
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
        Creates and saves a superuser with the given email and full name.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, full_name, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model using email as the unique identifier.
    """

    email = models.EmailField(max_length=50, unique=True, db_index=True, verbose_name="E-mail")
    full_name = models.CharField(max_length=75, verbose_name="ФИО")
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Позиция",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Департамент",
    )
    phone_number_work = PhoneNumberField(verbose_name="Рабочий телефон")
    phone_number_personal = PhoneNumberField(verbose_name="Личный телефон")
    # Другие поля
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return f"Пользователь {self.full_name} {self.email}"
