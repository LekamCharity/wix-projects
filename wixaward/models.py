from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    prof_picture = models.ImageField(upload_to="images",default="https://ucarecdn.com/d25b21e0-4072-48e4-8ad6-6571892f2450/ava.png")
    name = models.CharField(max_length=50,blank=True)
    bio = models.TextField(max_length=600,default="My Bio",blank=True)
    contact = models.EmailField(max_length=300,blank=True)
    location = models.CharField(max_length=70,blank=True)


    def __str__(self):
        return f"{self.user.username } Profile"

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    technology = models.CharField(max_length=300,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    date = models.DateTimeField(auto_now_add=True,blank=True)
    url = models.URLField(max_length=300)
    photo = ImageField(manual_crop='1280x720')
    

    def __str__(self):
        return f"{self.title}"

    def delete_post(self):
        return self.delete

    def save_post(self):
        return self.save()

    @classmethod
    def all_post(cls):
        return cls.objects.all()

    @classmethod
    def get_languages(cls,language):
        language = Post.objects.filter(language=language).all()
        return language

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()


class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='ratings',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='rater')
    content = models.IntegerField(choices=rating,blank=True)
    design = models.IntegerField(choices=rating,blank=True)
    usability = models.IntegerField(choices=rating,blank=True)
    score = models.FloatField(default=0,blank=True)
    content_coverage = models.FloatField(default=0,blank=True)
    design_coverage = models.FloatField(default=0,blank=True)
    usability_coverage = models.FloatField(default=0,blank=True)

    def save_ratings(self):
        return  self.save()

    def __str__(self):
        return f"{self.post} Rating"




