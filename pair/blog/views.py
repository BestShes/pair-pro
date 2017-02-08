from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


# Create your views here.

def post_list(request):

    post = Post.objects.all().order_by('-created_date')

    context = {
        'post_list': post

    }

    return render(request, 'blog/post-list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post_detail': post
    }
    return render(request, 'blog/post-detail.html', context)