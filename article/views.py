from django.shortcuts import render, get_object_or_404, redirect, reverse, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

import markdown

from .models import Post
from .forms import PostForm
from main.models import Category
from account.models import UserProfile


def posts(request):
    post_list = Post.objects.all()
    cat_list = Category.objects.all()
    return render(request, 'article/posts.html', {'post_list': post_list,
                                                  'cat_list': cat_list})


def cat_post(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    post_list = Post.objects.filter(category=cat)
    cat_name = cat.name
    cat_list = Category.objects.all()
    return render(request, 'article/posts.html', {'post_list': post_list,
                                                  'cat_list': cat_list,
                                                  'cat_name': cat_name})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    if post.mark_down:
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])

    user = request.user
    liked = False
    profiled = False
    if user.is_authenticated():
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return render(request, 'article/post_detail.html', {'post': post, 'profiled': profiled})
        profiled = True
        if post in profile.likes.all():
            liked = True
    return render(request, 'article/post_detail.html', {'post': post, 'liked': liked, 'profiled': profiled})


def post_author(request, username):
    if username == request.user.username:
        return redirect(reverse('article:post_person'))
    post_list = get_list_or_404(Post, auth__username=username)
    return render(request, 'article/posts.html', {'post_list': post_list,
                                                  'username': username})


@login_required
def post_person(request):
    user = request.user
    person = True
    post_list = Post.objects.filter(auth=user)
    return render(request, 'article/posts.html', {'post_list': post_list,
                                                  'person': person})


@login_required
def post_add(request):
    form = PostForm()
    user = request.user
    try:
        UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return render(request, 'account/profile_need.html')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth = user
            post.save()
            return redirect(reverse('article:post_detail', args=(post.pk,)))
        else:
            print(form.errors)

    return render(request, 'article/post_add.html', {'form': form})


@login_required
def post_edit(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    if post.auth != user:
        return redirect(reverse('index'))

    form = PostForm()
    form['title'].initial = post.title
    form['excerpt'].initial = post.excerpt
    form['body'].initial = post.body
    form['category'].initial = post.category
    form['mark_down'].initial = post.mark_down
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # 注意：此处不可直接使用form.save()，这样会新创建一个文章
            post.title = form.cleaned_data['title']
            post.excerpt = form.cleaned_data['excerpt']
            post.body = form.cleaned_data['body']
            post.category = form.cleaned_data['category']
            post.mark_down = form.cleaned_data['mark_down']
            post.save()
            return redirect(post)
        else:
            print(form.errrors)

    return render(request, 'article/post_edit.html', {'form': form,
                                                      'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user != post.auth:
        redirect('index')

    title = post.title
    post.delete()
    return render(request, 'article/post_delete.html', {'delete_title': title})


@login_required
def post_like(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']
    likes = 0
    if post_id:
        post = Post.objects.get(id=(int(post_id)))
        if post:
            user = request.user
            profile = UserProfile.objects.get(user=user)
            profile.likes.add(post)
            likes = post.userprofile_set.count()
            post.likes = likes
            post.save()
    return HttpResponse(likes)


@login_required
def post_like_cancel(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']
    likes = 0
    if post_id:
        post = Post.objects.get(id=(int(post_id)))
        if post:
            user = request.user
            profile = UserProfile.objects.get(user=user)
            profile.likes.remove(post)
            likes = post.userprofile_set.count()
            post.likes = likes
            post.save()
    return HttpResponse(likes)
