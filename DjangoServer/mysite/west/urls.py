from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^staff/', 'west.views.staff'),
	url(r'^templay/', 'west.views.templay')
)
