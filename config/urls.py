"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main_app.views import *
from user_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('odeme',payment,name='payment'),
    path('ok/',success,name='success'),
    path('fail/',fail,name='fail'),
    path('result/',result,name='result'),
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('aboutus',aboutus,name='aboutus'),
    path('blog',blog,name='blog'),
    path('blog/<id>',blogDetail,name='blogdetail'),
    path('donate',donate,name='donate'),
    path('involved',involved,name='involved'),
    path('ourwork',ourwork,name='ourwork'),
    path('whyoralhealt',whyoralhealt,name='whyoralhealt'),
    path('ckeditor/', include('ckeditor_uploader.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
