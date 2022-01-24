from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from state.models import Post
from django.contrib import messages
from state.models import Comment
from state.models import PostComment
import datetime

def home(request):
    if request.method == "POST":
        search = request.POST['search']
        post = Post.objects.filter(post_title=search)  
    else:
        messages.info(request,"Not Found ...")
        post = Post.objects.all()
    return render(request,'index.html',{'p':post})

  

def login(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect("/")
        else:
            messages.info(request,"UserName and Password Incorrect")
            return redirect("login")
    else:
        return render(request,"login.html")

    


def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect("login")
        else:
            return redirect("register")        
    else:
        return render(request,"register.html")         

def images(request):
    post = Post.objects.all()  
    return render(request, "images.html",{'p':post})

def logout(request):
    auth.logout(request)
    return redirect('/')          

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        time = datetime.datetime.now()
        comment = Comment.objects.create(name=name,email=email,subject=subject,message=message,time=time)
        return redirect('contact')
    else:
        post = Post.objects.all()  
        return render(request,"contact.html",{'p':post})   

def detail(request):
    if request.method == "GET":
        post_id = request.GET['id']
        if request.method == "POST":
            pl = PostComment()
            pl.id = request.GET['id']
            pl.Pname = request.POST['pname']
            pl.Pemail = request.POST['pemail']
            pl.Psubject = psubject = request.POST['psubject']
            pl.Pmessage =  request.POST['pmessage']
            pl.save()
    post = Post.objects.filter(id=post_id)
    return  render(request, "detail.html",{'p':post})     






def profile(request):
    if request.method == "POST":
        login_name = request.GET['user']
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        uuser = User.objects.get(first_name=login_name)
        uuser.first_name=first_name
        uuser.last_name=last_name
        uuser.email = email
        uuser.username = user_name
        uuser.save()
        return redirect('/profile?user={login_name}')
    else:
        pass    
    return render(request, "profile.html")


def adminpage(request):
    return render(request, "adminpage.html")