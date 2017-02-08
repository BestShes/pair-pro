from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.admin import User


# Create your views here.

def post_list(request):
    post = Post.objects.all().order_by('-created_date')

    context = {
        'post_list': post

    }

    return render(request, 'blog/post-list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post_detail': post
    }
    return render(request, 'blog/post-detail.html', context)


def post_add(request):
    if request.method == 'POST':
        data = request.POST
        title = data['input_title']
        content = data['input_text']
        author = User.objects.create_user(username=data['input_name'],email='dd@dd.com', password='22')

        Post.objects.create(title=title, text=content, author=author)
        return redirect('post_list')


    return render(request, 'blog/post-add.html')
