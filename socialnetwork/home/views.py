from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from home.models import Post
from django.contrib.auth.models import User


# Create your views here.

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/home.html', {'posts': posts})

class PostDetailView(View):
    template_name = 'home/postDetail.html'
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, self.template_name, {'post': post} )


class ProfileView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        userPosts = Post.objects.filter(author=user.username)
        return render(request, 'home/profileView.html', {'user': user, 'userPosts': userPosts})

