from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class CustomManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')
        
        if not phone:
             raise ValueError('User must have an phone number')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone = phone,          
        )
        
        user.set_password(password)
        #user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, phone, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            phone=phone,                 
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    
    username     =models.CharField(max_length=50,unique=True)
    email        =models.EmailField(max_length=100,unique=True)
    phone =models.CharField(max_length=12, unique=True)
    
    date_joined  =models.DateTimeField(auto_now_add=True)
    last_login   =models.DateTimeField(auto_now_add=True)
    is_admin     =models.BooleanField(default=False)
    is_staff     =models.BooleanField(default=False)
    is_active    =models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    
    objects = CustomManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
