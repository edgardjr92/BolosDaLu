from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from BolosDaLu import settings
from bolosdaluapp.views import index_view, about_view, services_view, gallery_view, testimonials_view, contact_view
from bolosdaluapp.views.about_view import AboutView
from bolosdaluapp.views.contact_view import ContactView
from bolosdaluapp.views.gallery_view import GalleryView
from bolosdaluapp.views.index_view import IndexView
from bolosdaluapp.views.services_view import ServicesView
from bolosdaluapp.views.testimonials_view import TestimonialsView

admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BolosDaLu.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', IndexView.as_view()),
                       url(r'^sobre/', AboutView.as_view()),
                       url(r'^servicos/', ServicesView.as_view()),
                       url(r'^galeria/', GalleryView.as_view()),
                       url(r'^depoimentos/', TestimonialsView.as_view()),
                       url(r'^contato/', ContactView.as_view()),
                       url(r'^fotos/([0-9]+)/', GalleryView.fotos),
                       url(r'^add/', TestimonialsView.add),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^static/media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document.root': settings.MEDIA_ROOT}),
    )
