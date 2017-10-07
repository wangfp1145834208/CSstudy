from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm, PassChangeForm

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='account/login.html',
                                     form_class=LoginForm,
                                     redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name='account/logout.html'),
        name='logout'),

    url(r'^password_change/$',
        auth_views.PasswordChangeView.as_view(template_name='account/password_change.html',
                                              form_class=PassChangeForm),
        name='password_change'),
    url(r'^password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
        name='password_change_done'),

    url(r'^profile/$', views.profile_show, name='profile_show'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
]