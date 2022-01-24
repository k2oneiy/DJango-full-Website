from django.urls import path
from . import views



urlpatterns = [
    path('/',views.adminpage,name="login"),
    path('/posts',views.posts,name="posts"),
    path('/addpost',views.addpost,name="addpost"),
    path('/posts/edit',views.editpost,name="edit"),
    path('/posts/delete',views.delete,name="delete"),
]