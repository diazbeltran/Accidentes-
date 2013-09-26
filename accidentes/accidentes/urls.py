from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin





admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   # url(r'^$', 'accidente.views', name='inicio()'),
    #url(r'^accidente/', include('accidente.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#   url(r'^$','datos.views.lista_accidentes'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$','datos.views.ingresar'), 
   url(r'^usuario/nuevo$','datos.views.nuevo_usuario'),
   url(r'^ingresar/$','datos.views.ingresar'),	
   url(r'^privado/$','datos.views.privado'),
   url(r'^cerrar/$', 'datos.views.cerrar'),
   url(r'^principal', 'datos.views.principal'), 
   url(r'^admin/datos/accidente/', 'datos.views.principal'),
   url(r'^administracion/$', 'datos.views.administracion'),
   
)
