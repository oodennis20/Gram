from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo= ImageField(blank=True,manual_crop='')
    bio= models.CharField(max_length=240, null=True)
    

    @receiver(post_save, sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):  
        profile= Profile.objects.all()
        return profile
    
    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile
    
class Image(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    insta_image = ImageField(blank=True,manual_crop='')
    caption = models.TextField(null=True)
    # likes = models.PositiveIntegerField(default=0)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    
    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return Image

    def __str__(self):
        return str(self.caption)

class Comment(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments',null=True)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment
        
class Follow(models.Model):
    users=models.ManyToManyField(User,related_name='follow')
    current_user=models.ForeignKey(User,related_name='c_user',null=True)

    @classmethod
    def follow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.add(new)

    @classmethod
    def unfollow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.remove(new)
        




