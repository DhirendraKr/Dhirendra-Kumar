from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils import timezone



# class UserManager(BaseUserManager):
#     use_in_migrations = True
#     def create_user(self, username, user_id, email, password=None):
#
#         '''
#         Creates and saves a user with basic information
#         The user is inactive until a password is set.
#         '''
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         if not username:
#             raise ValueError('Users must have a username')
#
#         user = self.model(
#             user_id = user_id,
#             username = username,
#             email = self.normalize_email(email),
#             is_active = False,
#             user_create_date = timezone.now(),
#         )
#
#         if not password:
#             user.set_unusable_password()
#         else:
#             user.set_password(password)
#
#         user.save(using=self._db)
#         return user
#
#
#     def create_superuser(self, username, user_id, email, password):
#
#         user = self.create_user(username, user_id, email, password)
#
#         user.is_active = True
#         user.is_staff = True
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using=self._db)
#
#         return user


class User(AbstractUser):
    username                    = models.CharField(max_length=254, unique=True, db_column='username')
    email                       = models.CharField(max_length=254, unique=True, db_column='email')
    user_create_date            = models.DateTimeField(default=timezone.now, db_column='user_create_date')
    user_password_change_date   = models.DateTimeField(null=True, db_column='user_password_change_date')
    is_active                   = models.BooleanField(default=False, db_column='is_active')
    is_staff                    = models.BooleanField(default=False, db_column='is_staff')
    is_admin                    = models.BooleanField(default=False, db_column='is_admin')

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['user_id', 'email']
    # objects = UserManager()
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        constraints = [
            models.UniqueConstraint(fields=['username'], name='UK1_USER'),
            models.UniqueConstraint(fields=['email'], name='UK2_USER')
        ]

    def __str__(self):
        return self.username


class City(models.Model):
    city_id     = models.AutoField(primary_key=True, db_column='city_id')
    city_name   = models.CharField(max_length=60, db_column='city_name')
    is_default  = models.BooleanField(default=False, db_column='is_default')

    def __str__(self):
        return "%s " % (self.city_id)

    class Meta:
        db_table = 'city'
        verbose_name = "City"
        verbose_name_plural = "Citys"


