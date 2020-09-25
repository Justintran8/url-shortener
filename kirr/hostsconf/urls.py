from django.urls import include, path
from django.contrib import admin
from .views import wildcard_redirect

admin.autodiscover()

urlpatterns = [
    #path('/', admin.site.urls),
    path('', wildcard_redirect),
]