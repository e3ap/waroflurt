"""WarofLurt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.Games.as_view() , name = 'games_list'),
    re_path('^play/save/(?P<pk>\d+)/$', views.GamePlay.as_view(), name = 'gameplay'),
    re_path('^saves/(?P<pk>\d+)/$', views.Saves.as_view(), name = 'saves_list'),
    path('delete/<int:pk>', views.DeleteSave.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateSave.as_view(), name='update')
]
