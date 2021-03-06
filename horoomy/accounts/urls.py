from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .models import Verification
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^restore/$', views.restore, name='restore'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^password/$', views.edit_password, name='password-edit'),

    url(r'^register/confirm/(?P<key>.+)/$', views.confirm,
        {'vn_action': Verification.REG, 'template_name': 'accounts/register_done.html'}, name='register-confirm'),
    url(r'^restore/confirm/(?P<key>.+)/$', views.confirm,
        {'vn_action': Verification.PASS, 'template_name': 'accounts/restore_done.html'}, name='restore-confirm'),

    url(r'^social-auth/creditals/$', views.creditals, name='creditals'),
    url(r'^social-auth/', include('allauth.urls')),
]
