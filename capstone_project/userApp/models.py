from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Profile1(models.Model):
    #user = models.OneToOneField(User,on_delete = models.CASCADE)
    mobile = models.IntegerField()
    company_name = models.CharField(max_length=200)
    company_information = models.TextField()

    def __str__(self):
        return str(self.user.username)

class Profile3(models.Model):  #for person who find job
    unique_together = (('Name','Email'),)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    qualification = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date1 = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,related_name= 'post',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('sppost',kwargs={'id1':self.pk})

class UpdatePost(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    no_of_opening = models.IntegerField(null = False)
    skills = models.CharField(max_length=300)
    experience =  models.CharField(max_length=100)

class comment(models.Model):  #for person who find job and Apply
    post = models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    name = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    create_date = models.DateTimeField(default = timezone.now)
    email = models.EmailField(max_length=100)
    qualification =  models.CharField(max_length=100)
    skills = models.CharField(max_length=300)
    experience =  models.CharField(max_length=100)
    approved_comment = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.author)