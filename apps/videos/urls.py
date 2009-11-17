from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # all tags
    url( r'^$', 'videos.views.list', name='videos_list'),
    url( r'^add/$', 'videos.views.add', name='videos_add'),
    url( r'^update/(?P<slug>[-\w]+)/$', 'videos.views.update', name='videos_update'),
    url( r'^(?P<slug>[-\w]+)/$', 'videos.views.detail', name='videos_detail'),
)

