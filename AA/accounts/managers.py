import email

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email,username,password=None):
        if not email:
            raise ValueError("vared kardan email ejbarist")
        if not phone_number:
            raise ValueError("vared kardan phone ejbarist")
        user = self.model(
            first_name= first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        pass
    user = self.create_user(self, phone_number,first_name,lastname, email,username,password)
    user.is_admin = True