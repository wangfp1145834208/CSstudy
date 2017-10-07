from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileForm
from .models import UserProfile
from article.models import Post


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    form = UserForm()
    registered = False

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
        else:
            print(form.errors)

    return render(request, 'account/register.html', {'form': form,
                                                     'registered': registered})


@login_required
def profile_show(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return render(request, 'account/profile_need.html')
    posts = Post.objects.filter(auth=request.user).order_by('-modified_time')[:3]
    likes = profile.likes.all()
    collections = profile.collections.all()
    context = {'profile': profile, 'posts': posts, 'likes': likes, 'collections': collections}
    return render(request, 'account/profile_show.html', context=context)


@login_required
def profile_edit(request):
    form = UserProfileForm()

    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
            profile = UserProfile(user=user)
    else:
        # 此处需要注意不能直接使用field.widget
        # 因为UserProfileForm继承的是forms.ModelForm，而该类中的field都是BoundField
        form['last_name'].initial = profile.user.last_name
        form['first_name'].initial = profile.user.first_name
        form['email'].initial = profile.user.email
        form['nickname'].initial = profile.nickname
        form['birth'].field.widget.attrs['value'] = profile.birth
        form['signature'].initial = profile.signature

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.email = form.cleaned_data['email']
            profile.birth = form.cleaned_data['birth']
            profile.nickname = form.cleaned_data['nickname']
            profile.signature = form.cleaned_data['signature']
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            user.save()
            profile.save()
            return redirect(reverse('profile_show'))
        else:
            print(form.errors)

    return render(request, 'account/profile_edit.html', {'form': form, 'profile': profile})
