# from django.conf.urls import include, url
# from django.contrib import admin
from django.conf.urls import url
from . import view
urlpatterns = [
    # Examples:
    # url(r'^$', 'PrometheusOneAlert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view.send_alert),
]
