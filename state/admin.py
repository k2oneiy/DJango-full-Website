from django.contrib import admin
from state.models import Post
from state.models import Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
