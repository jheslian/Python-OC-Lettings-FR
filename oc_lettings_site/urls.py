from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .tests import trigger_error

app_name = 'oc_site'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path('sentry-debug', trigger_error),
]
