from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'oc_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
]
