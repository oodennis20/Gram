from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    comments = Comment.objects.all()
    return render(request,"home.html",{"images":images,"comments":comments})

@login_required
def profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
    images = Image.objects.filter()

    return render(request,"profile.html",{"profile":profile,"images":images})


def search_results(request):

    if 'image' in request.GET and request.GET['image']:
        search_images = request.GET.get("image")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    image = Image.objects.get(id = image_id)

    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.name = current_user
            image.save()
        return redirect('home')

    else:
        form = CommentForm()

    return render(request,"image.html", {"image":image,"form": form})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def update_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.name = current_user
            image.save()
        return redirect('home')

    else:
        form = UploadForm()
    return render(request, 'upload.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.name = current_user
            image.save()
        return redirect('home')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})