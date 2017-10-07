from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Website
from .forms import WebsiteForm
from main.models import Category
from account.models import UserProfile


def websites(request):
    cat_list = Category.objects.all()
    web_list = Website.objects.all()
    user = request.user
    profile = None
    if user.is_authenticated():
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return render(request, 'account/profile_need.html')
    return render(request, 'collection/website.html', {'cat_list': cat_list,
                                                       'web_list': web_list,
                                                       'profile': profile})


def cat_web(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    web_list = Website.objects.filter(category=cat)
    user = request.user
    profile = None
    if user.is_authenticated():
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return render(request, 'account/profile_need.html')
    return render(request, 'collection/website.html', {'cat_name': cat.name,
                                                       'web_list': web_list,
                                                       'profile': profile})


@login_required
def add_website(request):
    form = WebsiteForm()
    user = request.user
    try:
        UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return render(request, 'account/profile_need.html')

    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('collection:websites'))
        else:
            print(form.errors)

    return render(request, 'collection/add_website.html', {'form': form})


@login_required
def web_collected(request):
    web_id = None
    if request.method == 'GET':
        web_id = request.GET['web_id']
    website = get_object_or_404(Website, pk=int(web_id))
    profile = UserProfile.objects.get(user=request.user)
    profile.collections.add(website)
    website.collected = website.userprofile_set.count()
    website.save()
    return HttpResponse('<span class="label label-default">已收藏</span>')


@login_required
def collected_cancel(request):
    col_id = None
    if request.method == 'GET':
        col_id = request.GET['col_id']
    website = get_object_or_404(Website, pk=int(col_id))
    profile = UserProfile.objects.get(user=request.user)
    profile.collections.remove(website)
    website.collected = website.userprofile_set.count()
    website.save()
    return HttpResponse('OK')
