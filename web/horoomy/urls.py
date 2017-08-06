from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('core.urls')),
    url(r'^docs/', include('docs.urls')),
    url(r'^', include('parsers.urls')),
]
