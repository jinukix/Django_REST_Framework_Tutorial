from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls'))
]