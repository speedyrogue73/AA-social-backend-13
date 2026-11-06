from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, email, username, password=None):
        if not email:
            raise ValueError("vared kardan email ejbarist")
        if not phone_number:
            raise ValueError("vared kardan phone ejbarist")

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, last_name, email, username, password=None):
        user = self.create_user(phone_number, first_name, last_name, email, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
