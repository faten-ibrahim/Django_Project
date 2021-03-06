"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from user_app import views


app_name='user_app'

urlpatterns = [
    url(r'^register/$',views.register,name="register"),
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^profile/$',views.user_profile,name="user_profile"),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^updateprofile/$',views.user_update_profile,name='update_profile'),


]
