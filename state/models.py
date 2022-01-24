from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='pics')
    post_con = models.CharField(max_length=300)
    post_author = models.CharField(max_length=50)
    post_date = models.DateTimeField()
    post_comment_count = models.IntegerField()
    post_tag = models.CharField(max_length=30)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=500)
    time = models.DateTimeField()
    
class PostComment(models.Model):
    Ptitle = models.CharField(max_length=100)
    Pname = models.CharField(max_length=200)
    Pdatetime = models.DateField()
    Pemail = models.EmailField(max_length=50)
    Psubject = models.CharField(max_length=200)
    Pmessage = models.CharField(max_length=100)






