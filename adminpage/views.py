from django.shortcuts import render,redirect
from state.models import Post
import datetime
from django.contrib.auth.models import User , auth



def adminpage(request):
    return render(request,"adminpage.html")


def posts(request):
    post = Post.objects.all()
    return render(request, "posts.html",{'p':post})    


def addpost(request):
    if request.method == "POST":
        add = Post()
        add.post_title = request.POST.get('title')
        add.post_author = request.POST.get('author')
        add.post_con = request.POST.get('content')
        add.post_img = request.FILES['file']
        add.post_tag = request.POST.get('tag')
        add.post_date = datetime.datetime.now()
        add.post_comment_count = 0
        add.save()
        return redirect('addpost')
    return render(request, "addpost.html")    



def editpost(request):
    editid = request.GET['id']
    post = Post.objects.filter(id=editid)
    editpost = Post.objects.get(id=editid)
    if request.method == "POST":
        editpost.post_title = request.POST['title']
        editpost.post_author = request.POST['author']
        editpost.post_con = request.POST['content']
        editpost.post_img = request.FILES.get('file', False)
        editpost.post_tag = request.POST['tag']
        editpost.post_date = datetime.datetime.now()
        editpost.post_comment_count = 0
        editpost.save()
        return redirect('/adminpage/posts')
    return render(request, "editpost.html",{'p':post})  


def delete(request):
    if request.method == "GET":
        id = request.GET['id']
        post = Post.objects.filter(id=id).delete();
        return redirect('/adminpage/posts')
    return render(request, "posts.html")    