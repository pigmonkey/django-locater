from django.conf.urls.defaults import *
from locater.views import find_nearest

urlpatterns = patterns('',
    (r'^$', find_nearest),
)
