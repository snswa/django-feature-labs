from django.conf.urls.defaults import *

urlpatterns = patterns('featurelabs.views',
    url(r'^$', 'index', name='featurelabs_index'),
)
