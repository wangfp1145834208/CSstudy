from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Category, Tag
from .forms import CategoryForm
from article.models import Post
from collection.models import Website
from account.models import UserProfile



def to_index(request):
    return index(request)


def index(request):
    cat_list = Category.objects.all()
    tag_list = Tag.objects.all()
    post_list = Post.objects.all().order_by('-likes')[:3]
    web_list = Website.objects.all()[:5]
    return render(request, 'index.html', {'cat_list': cat_list,
                                          'tag_list': tag_list,
                                          'post_list': post_list,
                                          'web_list': web_list})


@login_required
def add_category(request):
    form = CategoryForm()
    user = request.user
    try:
        UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return render(request, 'account/profile_need.html')

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():  # 注意此处是is_valid()，而不是is_valid
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors)

    return render(request, 'main/add_category.html', {'form': form})
