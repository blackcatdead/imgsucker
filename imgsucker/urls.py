"""imgsucker URL Configuration

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
from django.urls import path, include
from imgsucker import views_admin as va
from imgsucker import views_front as vf
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

urlpatterns = [
    # path('auth/', include('social_django.urls', namespace='social')),
    path('auth/', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),
    path('suckimage', va.suckimage, name='suckimage'),

    path('admin2/login', va.login, name='login2'),
    path('admin2', va.home, name='home2'),
    path('admin2/logout', va.logout, name='logout2'),
    path('admin2/sucking', va.grab, name='grab'),
    path('admin2/suckinghost/wallpaperscraft_com', va.grabhost_wallpaperscraft0com, name='grabhost_wallpaperscraft0com'),





    path('ajax/ajax_grab', va.ajax_grab, name='ajax_grab'),
    path('ajax/ajax_refreshresult', va.ajax_refreshresult, name='ajax_refreshresult'),
    path('ajax/ajax_submitwallpaper', va.ajax_submitwallpaper, name='ajax_submitwallpaper'),
    path('ajax/ajax_grabhost_wallpaperscraft0com_single', va.ajax_grabhost_wallpaperscraft0com_single, name='ajax_grabhost_wallpaperscraft0com_single'),

    path('json/tags', va.json_tags, name='json_tags'),

    path('test', va.test, name='test'),

    path('archive/<int:wallpaper_resolution_id>/<slug:title>.jpg/', va.archive, name='archive'),





    path('', vf.home, name='fr_home'),
    path('all/<str:sort>/page-<int:page>', vf.all, name='fr_all'),
    path('search', vf.search, name='fr_search'),
    path('wallpaper/<str:tags>_<int:id>', vf.wallpaper, name='fr_wallpaper'),

    path('tag/<str:tag>', vf.tag, name='fr_tag'),
    path('tag/<str:tag>/<str:sort>/page-<int:page>', vf.tag, name='fr_tag'),

    path('color/<str:color>', vf.color, name='fr_color'),
    path('color/<str:color>/<str:sort>/page-<int:page>', vf.color, name='fr_color'),

    path('category/<slug:category>', vf.category, name='fr_category'),
    path('category/<slug:category>/<str:sort>/page-<int:page>', vf.category, name='fr_category'),

    path('download/<str:title>_<int:id_wall>/<int:w>x<int:h>', vf.download, name='fr_download'),

    path('image/<str:title>_<int:id_wall>_<int:w>x<int:h>.jpg', vf.image, name='fr_image'),

    path('tags', vf.tag, name='fr_tag'),


    path('user/login', vf.loginclient, name='fr_login'),
    path('user/needlogin', vf.needloginclient, name='fr_needlogin'),
    path('user/logout', vf.logoutclient, name='fr_logout'),
    path('user/register', vf.registerclient, name='fr_register'),
    path('user', vf.user, name='fr_user'),
    path('user/profile/<str:username>', vf.userprofile, name='fr_userprofile'),
    path('user/edit/', vf.useredit, name='fr_useredit'),
    path('ajax/useraction', vf.ajaxuseraction, name='ajax_useraction'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)