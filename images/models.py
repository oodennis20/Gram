from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='snap/', null=True)
    bio= models.CharField(max_length=240, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    @classmethod
    def my_profile(cls,id):
        profile= cls.objects.filter(id=id)
        return profile
    
    class Meta:
        ordering = ['user']

class Comment(models.Model):
    comment = models.CharField(max_length=70, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    imagecomment= models.ForeignKey('images.Image',on_delete=models.CASCADE, related_name='image', null=True)

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment
        
class Image(models.Model):
    insta_image = models.ImageField(upload_to='snap/', null=True)
    caption = models.CharField(max_length=70, null=True)
    like=models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts', null=True)
    thoughts = models.ForeignKey(Comment,on_delete=models.CASCADE, null=True)
    profile= models.ForeignKey(Profile, null=True)

    @classmethod
    def all_images(self):

        return Image.objects.all()
    
    @classmethod
    def get_user_images(cls, profile_id):
        images=Image.objects.filter(profile_id=user.id)
        
class Likes(models.Model):
    likes= models.IntegerField (default=0)
    liker = models.CharField(max_length=20)

        




