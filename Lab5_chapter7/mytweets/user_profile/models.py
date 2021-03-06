from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
	"""
	Custom user class.
	"""
	username = models.CharField('username', max_length=10,  
	unique=True, db_index=True) 
	email = models.EmailField('email address', unique=True) 
	joined = models.DateTimeField(auto_now_add=True) 
	is_active = models.BooleanField(default=True) 
	is_admin = models.BooleanField(default=False)
	
	USERNAME_FIELD = 'username'
	def __unicode__(self):
		return self.username
		
class UserFollower(models.Model):
	user = models.ForeignKey(User, unique=True,on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	count = models.IntegerField(default=1)
	followers = models.ManyToManyField(User,related_name='followers')
	def __str__(self):
		return '%s, %s' % self.user, self.count 