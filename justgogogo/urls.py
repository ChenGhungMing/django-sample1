"""justgogogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from justapp.views import hello_world
from justapp.views import index
from justapp.views import blank
from justapp.views import blank1
from justapp.views import blank2
from justapp.views import blank3
from justapp.views import buttons
from justapp.views import flot
from justapp.views import forms
from justapp.views import grid
from justapp.views import icons
from justapp.views import login
from justapp.views import morris
from justapp.views import notifications
from justapp.views import panels_wells
from justapp.views import tables
from justapp.views import typography
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('justadmin/', admin.site.urls),
    path('hello/', hello_world),
    path('index/', index),
    path('blank/', blank),
    path('blank1/', blank1),
    path('blank2/',blank2),
    path('blank3/',blank3),
    path('buttons/',buttons),
    path('flot/',flot),
    path('forms/',forms),
    path('grid/',grid),
    path('icons/',icons),
    path('login/',login),
    path('morris/',morris),
    path('notifications/',notifications),
    path('panels_wells/',panels_wells),
    path('tables/',tables),
    path('typography/',typography),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
