
from django.contrib import admin
from django.urls import path
from uyga.views import uyga
urlpatterns = [
    path('',uyga),
    path('admin/', admin.site.urls),
]
