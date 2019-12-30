from django import forms
from .models import Image, Profile, Comment
from .models import *

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']  

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['posted_by', 'profile']  

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        exclude =['poster','image']