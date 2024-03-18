from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-created_at')
	return render (request, 'index.html', {'posts': posts})

def post(request, pk):
	posts =Post.objects.get(id=pk)
	return render (request, 'post.html', {'posts': posts})