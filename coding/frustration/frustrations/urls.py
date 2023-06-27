"""frustrations URL Configuration

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
from django.contrib import admin
from user import views as user_views
from mindsparkadmin import views as mindsparkadmin_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$', user_views.index, name="index"),
    url('user/register',user_views.register,name="register"),
    url('user/userpage',user_views.userpage,name="userpage"),
    url('user/motivationalmegpage/(?P<pk>\d+)/(?P<select>\w+)/$',user_views.motivationalmegpage,name="motivationalmegpage"),
    url('user/notmotivationalmegpage/(?P<pk>\d+)/(?P<session>\w+)/$',user_views.notmotivationalmegpage,name="notmotivationalmegpage"),
    url('user/selectsessionpage',user_views.selectsessionpage,name="selectsessionpage"),
    url('user/nonselectsessionpage',user_views.nonselectsessionpage,name="nonselectsessionpage"),
    url('user/mydetails',user_views.mydetails,name="mydetails"),
    url('user/updatemydetails',user_views.updatemydetails,name="updatemydetails"),
    url('user/viewnotification',user_views.viewnotification,name="viewnotification"),
    url('user/feedback',user_views.feedback,name="feedback"),
    url('admin/logout/$',user_views.logout,name='logout'),

    url('admin/login',mindsparkadmin_views.login,name="login"),
    url('admin/homepage',mindsparkadmin_views.homepage,name="homepage"),
    url('admin/chartpage/(?P<chart_type>\w+)/$',mindsparkadmin_views.chartpage,name="chartpage"),
    url('admin/viewuserdetails', mindsparkadmin_views.viewuserdetails, name="viewuserdetails"),
    url('admin/notification', mindsparkadmin_views.notification, name="notification"),
    url('admin/viewfeedback', mindsparkadmin_views.viewfeedback, name="viewfeedback"),
    url('admin/motivationalaresults', mindsparkadmin_views.motivationalaresults, name="motivationalaresults"),

]
