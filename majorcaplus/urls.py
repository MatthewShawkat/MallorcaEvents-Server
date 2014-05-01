from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'majorcaplus.views.home', name='home'),
    # url(r'^majorcaplus/', include('majorcaplus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'events.views.index', name='home'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/manage'}),
    url(r'^accounts/profile/$', RedirectView.as_view(url=reverse_lazy('manage'))),

    url(r'^email', 'events.views.email', name='email'),

    url(r'^manage', 'events.views.manage', name='manage'),
    url(r'^event/view', 'events.views.view', name='view'),
    url(r'^event/add', 'events.views.add', name='add'),
    url(r'^event/delete', 'events.views.delete', name='delete'),
    url(r'^event/update', 'events.views.update', name='update'),

    url(r'^category/view', 'events.views.viewcat', name='view'),
    url(r'^category/add', 'events.views.addcat', name='add'),
    url(r'^category/delete', 'events.views.deletecat', name='delete'),
    url(r'^category/update', 'events.views.updatecat', name='update'),

    url(r'^promotion/view', 'events.views.viewpro', name='view'),
    url(r'^promotion/add', 'events.views.addpro', name='add'),
    url(r'^promotion/delete', 'events.views.deletepro', name='delete'),
    url(r'^promotion/update', 'events.views.updatepro', name='update'),

    url(r'^event/image/add', 'events.views.imageadd', name='imageadd'),
    url(r'^event/image/delete', 'events.views.imagedelete', name='imagedelete'),

    url(r'^event/data', 'events.views.data', name='data'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
