from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    re_path('^accounts/profile/$', views.redirect_to_user_profile, name = 'redirect_user_detail'),
    re_path('^accounts/profile/(?P<pk>\d+)/', views.UserProfile.as_view(), name= 'user_detail'),
    re_path('^$', views.SignUp.as_view(), name = 'signup')
]

