from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^manageShipping/$', 'Alak.libraryPortal.views.manageShipping'),
    url(r'^borrow/', 'Alak.libraryPortal.views.borrowBooks'),
    url(r'^return/', 'Alak.libraryPortal.views.returnBooks'),
    url(r'^$', 'Alak.libraryPortal.views.libraryPortal'),
)
