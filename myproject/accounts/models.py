from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # Create your models here.






















# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('must have an email adress')
#         if not username:
#             raise ValueError('must have an username')

#         user = self.model(
#             email = self.normalize_email(email),
#             username = username
#         )

#         user.set_password(password)
#         user.save(user=self._db)
#         return user

#     def create_superuser(self,email,usesrname,password):
#         user = self.model(
#             email=self.normalize_email(email),
#             password=password,
#             username=usesrname,
#             )
#         user.is_admin=True
#         user.is_staff=True
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user


# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email', max_length=30, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=30, unique=True)
#     lasst_name = models.CharField(max_length=30, unique=True)
#     password = models.CharField(verbose_name='Password', max_length=30)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)


#     # changes the default username to email
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_lable):
#         return True


