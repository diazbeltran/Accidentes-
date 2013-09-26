from datos.models import *
from django.contrib import admin
from django.contrib.gis import admin




admin.site.register(Accidente, admin.OSMGeoAdmin)
admin.site.register(Calzada)
#admin.site.register(ClaseAccidente)
admin.site.register(Comisaria)
admin.site.register(Comuna)
#admin.site.register(Comuna2)
#admin.site.register(CondicionCalzada)
#admin.site.register(Demarcacion)
#admin.site.register(DemarcacionAccidente)
#admin.site.register(DetalleUbicacionRelativa)
#admin.site.register(EstadoAtmosferico)
#admin.site.register(Formulario)
#admin.site.register(Luminosidad)
admin.site.register(Maniobra)
admin.site.register(Personas)
admin.site.register(Region)
admin.site.register(Responsable)
#admin.site.register(Servicio)
#admin.site.register(SubSector)
#admin.site.register(TipoAccidente)
admin.site.register(TipoCalzada)
#admin.site.register(TipoVehiculo)
#admin.site.register(UbicacionRelativa)
admin.site.register(Vehiculo)
#admin.site.register(Vehiculo2)

