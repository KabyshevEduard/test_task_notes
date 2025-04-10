from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, login, name, password=None):
        if not login:
            raise ValueError('There is no login')
        
        if not name:
            raise ValueError('There is no name')
        
        user = self.model(login=login, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, name, password):
        user = self.create_user(login=login, name=name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
        

class MyUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(unique=True)
    name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.login
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, perm, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

class Notes(models.Model):
    title = models.CharField(max_length=255, blank=True)
    discription = models.TextField(blank=True, null=True)
    user = models.ForeignKey('MyUser', models.DO_NOTHING, blank=True, null=True)