"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from personal.views import(
    home_screen_view, login_view,register, sign_in_view,
    )

from account.views import(
    logbook_view, run_script,create_class,capture_view,run_script,video_feed,capture_photo, process_image,add_class_view,
    class_list_view,delete_view,
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_screen_view,name='home'),
    path("login.html/", login_view, name='login'),
    path('register/', register, name='register'),
    path("sign_in_view/", sign_in_view, name='sign_in_view'),
    path("logbook.html/", logbook_view,name='logbook'),
    path('capture.html/', capture_view, name='capture_view'),
    path('createclass.html/',create_class, name='create_class'),
    path('run_script', run_script, name="run_script"),
    path('video_feed', video_feed, name='video_feed'),
    path('capture_photo', capture_photo, name='capture_photo'),
    path('process_image', process_image, name='process_image'),
    path('add_class_view', add_class_view, name="add_class_view"),
    path('class_list_view', class_list_view,name="class_list_view"),
    path('delete_view/<int:class_id>/', delete_view,name="delete_view"),

]


