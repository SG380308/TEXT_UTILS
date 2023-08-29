"""
URL configuration for TEXT_UTILS project.

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
from django.urls import path
from .import views

# LECTURE 7 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('' , views.INDEX, name='INDEX'),
#     path('ABOUT' , views.ABOUT, name='ABOUT'),
# ]

#LECTURE 8

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('' , views.INDEX, name='INDEX'),
#     path('REMOVE_PUNCTUATION' , views.REMOVE_PUNCTUATION, name='REMOVE_PUNCTUATION'),
#     path('CAPITALIZE_FIRST' , views.CAPITALIZE_FIRST, name='CAPITALIZE_FIRST'),
#     path('NEW_LINE_REMOVE' , views.NEW_LINE_REMOVE, name='NEW_LINE_REMOVE'),
#     path('SPACE_REMOVE' , views.SPACE_REMOVE, name='SPACE_REMOVE'),
#     path('CHAR_COUNT' , views.CHAR_COUNT, name='CHAR_COUNT'),
# ]


#LECTURE 9

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('' , views.INDEX, name='INDEX'),
#     path('REMOVE_PUNCTUATION' , views.REMOVE_PUNCTUATION, name='REMOVE_PUNCTUATION'),
#     path('CAPITALIZE_FIRST' , views.CAPITALIZE_FIRST, name='CAPITALIZE_FIRST'),
#     path('NEW_LINE_REMOVE' , views.NEW_LINE_REMOVE, name='NEW_LINE_REMOVE'),
#     path('SPACE_REMOVE' , views.SPACE_REMOVE, name='SPACE_REMOVE'),
#     path('CHAR_COUNT' , views.CHAR_COUNT, name='CHAR_COUNT'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INDEX, name='INDEX'),
    path('SUBMIT/', views.SUBMIT, name='SUBMIT'),
]


