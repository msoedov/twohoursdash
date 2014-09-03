from django.conf.urls import patterns, url

urlpatterns = patterns(
    'twohours.views',
    url(r'^(?P<pk>\d+)/$', 'user_details', name='user_details'),
    url(r'^update/(?P<pk>\d+)/$', 'user_update', name='user_update'),
    url(r'^$', 'user_list', name='user_list'),
    url(r'^export$', 'user_csv', name='user_csv'),
)