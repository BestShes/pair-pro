from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, email=None):
        user = self.create_user(
            username,
            password=password,
            email=email,
        )
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class MyUser(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField
    following = models.ManyToManyField(
        'self',
        symmetrical= False,
        related_name="following_set"

    )
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(default=False)
    Objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def follow(self, userID):
        self.following.add(userID)

    def un_follow(self, userID):
        self.following.remove(userID)

    @property
    def follower(self):
        return list(self.following_set.all())