from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . managers import usermanager
class user(AbstractUser):
    phone_number = models.Charfield(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to="", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)



    objects = usermanager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email', 'username')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True





    @property
    def is_staff(self):
        return self.is_admin