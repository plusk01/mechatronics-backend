from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# import api

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mechatronics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include('api.urls')),

    # For dev use only
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
