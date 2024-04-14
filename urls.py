
from django.contrib import admin
from django.urls import path
from . import views
from operator import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("predict/", views.predict),
    path("predict/result", views.result),
]
