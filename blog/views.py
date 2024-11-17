from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView
from .forms import PostForm, CommentForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-created_at']

def PostDetailView(request, id):
    post= get_object_or_404(Post, pk=id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail',post.id)
    else:
        form = CommentForm()
    
    context={
        'post':post,
        'comments':comments,
        'form':form,
    }

    return render(request, 'blog/post-detail.html', context)

def PostCreateView(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect('home')
    else:
        post_form = PostForm()

    context = {
        'post_form' : post_form,
    }
    return render(request,'blog/add-post.html', context)

def PostUpdateView(request, id):
    post = get_object_or_404(Post,id=id)
    if request.method =='POST':
        post_edit = PostForm(request.POST, instance = post)

        if post_edit.is_valid():
            post_edit.save()

            return redirect('post-detail', post.id)
        
    else:
        post_edit = PostForm(instance=post)

    context = {
        'post_edit':post_edit
    }

    return render(request, 'blog/edit-post.html', context)

def PostDeleteView(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    
    context={
        'post':post,
    }
    return render(request,'blog/post-delete-confirm.html',context)