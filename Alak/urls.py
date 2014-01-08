from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
handler500 = 'Alak.misc.util.serverError'
handler404 = 'Alak.misc.util.pageNotFound'

urlpatterns = patterns('',

    url(r'^', include ('Alak.home.urls')),
    url(r'^libraryPortal/', include ('Alak.libraryPortal.urls')),
    # Examples:
    # url(r'^$', 'Alak.views.home', name='home'),
    # url(r'^Alak/', include('Alak.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
