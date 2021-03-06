"""class URL Configuration

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
from django.urls import path
from app01 import view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('classes/', view.classes),
    path('add_class/', view.add_class),
    path('del_class/', view.del_class),
    path('edit_class/', view.edit_class),
    path('teacher/', view.teacher),
    path('add_teacher/', view.add_teacher),
    path('del_teacher/', view.del_teacher),
    path('edit_teacher/', view.edit_teacher),
    path('student/', view.student),
    path('add_student/', view.add_student),
    path('del_student/', view.del_student),
    path('edit_student/', view.edit_student),

    path('edit_modal_class/', view.edit_modal_class),
    path('add_modal_student/', view.add_modal_student),
    path('edit_modal_student/', view.edit_modal_student),

    path('get_class_list/', view.get_class_list),
    path('add_modal_teacher/', view.add_modal_teacher),

    path('layout/', view.layout),
    path('login/', view.login),

]
