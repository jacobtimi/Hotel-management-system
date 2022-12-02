"""hotelmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from hotelmanagement.adminapp import views as admin_view 
from hotelmanagement.userapp import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_view.index_page, name="homepage"),
    path('homepage/', TemplateView.as_view(template_name="base_page.html"), name="homepage"),
    path('',TemplateView.as_view(template_name='index.html'),name="homepage"),
    path('about/',TemplateView.as_view(template_name='about.html'),name="About"),
    path('Services/',TemplateView.as_view(template_name='Services.html'),name="Services"),
    path('portfolio/',TemplateView.as_view(template_name='portfolio.html'),name="portfolio"),
    path('blog/',TemplateView.as_view(template_name='blog.html'),name="blog"),
    path('contact/',TemplateView.as_view(template_name='contact.html'),name="contact"),
    url(r'^ accounts/signup/$', admin_view.SignUpView.as_view(), name = "signup"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^username/(?P<user_id>\d+)/', admin_view.Profile, name='username'),
    url(r'^adminapp/', include('hotelmanagement.adminapp.urls')),
    url(r'^userapp/', include('hotelmanagement.userapp.urls')),
    ]






urlpatterns += staticfiles_urlpatterns()

