# -*- coding: utf-8 -*- 
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from __future__ import unicode_literals
from django.utils.encoding import force_bytes

from django.contrib.gis.db import models

class Accidente(models.Model):
    #acc_id = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo Accidente')
    fid = models.AutoField(primary_key=True,unique=True,verbose_name='Codigo Accidente')    
    ure = models.ForeignKey('UbicacionRelativa',verbose_name='Ubicacion Relativa')
    lum_cod = models.ForeignKey('Luminosidad', db_column='lum_cod',verbose_name='Luminosidad')
    veh = models.ForeignKey('Vehiculo', verbose_name='Vehiculo')
    #veh_patente = models.CharField(max_length=20,verbose_name='Patente')
    eta = models.ForeignKey('EstadoAtmosferico',verbose_name='Estado Atmosferico')
    #for_numero = models.ForeignKey('Formulario', db_column='for_numero',verbose_name='Formulario')
	
    cac = models.ForeignKey('ClaseAccidente',verbose_name='Clase Accidente')
	
    #sec = models.ForeignKey('SubSector',verbose_name='Sub Sector')
    tca_cod = models.ForeignKey('TipoCalzada', db_column='tca_cod',verbose_name='Tipo de Calzada')
    cal_cod = models.ForeignKey('Calzada', db_column='cal_cod', verbose_name='Código de la calzada')
    com_codigo = models.ForeignKey('Comuna', db_column='com_codigo',verbose_name='Comuna')
    con_cod = models.ForeignKey('CondicionCalzada', db_column='con_cod',verbose_name='Condicion Calzada')
    tac = models.ForeignKey('TipoAccidente',verbose_name='Tipo de Accidente')
    acc_fecha = models.DateTimeField(null=True, blank=True,verbose_name='Fecha')
    #acc_hora = models.DateTimeField(null=True, blank=True,verbose_name='Hora')
    acc_detalle = models.CharField(max_length=255, blank=True,verbose_name='Detalle')
    #acc_mensaje = models.CharField(max_length=255, blank=True,verbose_name='Mensaje')
    #acc_pista_ida = models.IntegerField(null=True,verbose_name='Pista id')
    acc_pista_reg = models.IntegerField(null=True,verbose_name='Pista Reg')
    #acc_estado_cal = models.IntegerField(null=True,verbose_name='Estado Calzada')
    acc_muertos = models.IntegerField(null=True,verbose_name='Muertos')
    acc_graves = models.IntegerField(null=True,verbose_name='Gravedad')
    acc_m_graves = models.IntegerField(null=True,verbose_name='M Gravedad')
    acc_leves = models.IntegerField(null=True,verbose_name='Leves')
    acc_calle_uno = models.CharField(max_length=255, blank=True,verbose_name='Calle uno')
    acc_calle_dos = models.CharField(max_length=255, blank=True,verbose_name='Calle dos')
    acc_altura = models.IntegerField(null=True,verbose_name='Altura')
    acc_parte = models.IntegerField(null=True,verbose_name='Parte')
    #acc_rolruta = models.CharField(max_length=255, blank=True,verbose_name='Rol Ruta')
    acc_kilometro = models.IntegerField(null=True,verbose_name='Kilometro')
    #acc_folio = models.IntegerField(null=True, blank=True,verbose_name='folio')
    geom = models.PointField()
    objects = models.GeoManager()
    class Meta:
        db_table = 'accidente2'
    def __unicode__(self):
        return force_bytes('%s' % (self.fid))
    
	

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Calzada(models.Model):
    cal_cod = models.IntegerField(primary_key=True,unique=True,
	verbose_name='Código de la calzada')
#    cal_cod = models.AutoField(primary_key=True)    
    cal_descricpion = models.CharField(max_length=255, blank=True, 
	verbose_name='Descripción de la calzada')
    class Meta:
        db_table = 'calzada'
    def __unicode__(self):
        return self.cal_descricpion

class ClaseAccidente(models.Model):
    cac_id = models.IntegerField(primary_key=True,unique=True,
         verbose_name='Clase de Accidente')
#    cac_id = models.AutoField(primary_key=True)
    cac_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'clase_accidente'
    def __unicode__(self):
        return self.cac_descripcion

class Comisaria(models.Model):
    cmr_codigo = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    cmr_codigo = models.AutoField(primary_key=True)
    cmr_nombre = models.CharField(max_length=255, blank=True,verbose_name='Nombre')
    class Meta:
        db_table = 'comisaria'
    def __unicode__(seft):
        return seft.cmr_nombre

class Comuna(models.Model):
    com_codigo = models.IntegerField(primary_key=True,unique=True)
#    com_codigo = models.AutoField(primary_key=True)
    reg_codigo = models.ForeignKey('Region', db_column='reg_codigo')
    com_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'comuna'
    def __unicode__(self):
        return self.com_nombre
   

class Comuna2(models.Model):
    com_codigo2 = models.IntegerField(primary_key=True,unique=True)
#    com_codigo2 = models.AutoField(primary_key=True)
    com_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'comuna2'
    def __unicode__(self):
        return self.com_nombre

class CondicionCalzada(models.Model):
    con_cod = models.IntegerField(primary_key=True,unique=True)
#    con_cod = models.AutoField(primary_key=True)
    con_ddescriocion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'condicion_calzada'
    def __unicode__(self):
        return self.con_ddescriocion

class Demarcacion(models.Model):
    dem_id = models.IntegerField(primary_key=True,unique=True)
#    dem_id = models.AutoField(primary_key=True)
    dem_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'demarcacion'
    def __unicode__(self):
        return self.dem_id

class DemarcacionAccidente(models.Model):
    dem_id = models.ForeignKey(Demarcacion)
    acc_id = models.ForeignKey(Accidente)
    class Meta:
        db_table = 'demarcacion_accidente'

class DetalleUbicacionRelativa(models.Model):
    ure_id2 = models.IntegerField(primary_key=True,unique=True)
#    ure_id2 = models.AutoField(primary_key=True)
    acc = models.ForeignKey(Accidente)
    dur_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'detalle_ubicacion_relativa'
    def __unicode__(self):
        return self.ure_id2

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class EstadoAtmosferico(models.Model):
    eta_id = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    eta_id = models.AutoField(primary_key=True)
    eta_descripcion = models.CharField(max_length=255, blank=True,verbose_name='Descripcion')
    class Meta:
        db_table = 'estado_atmosferico'
    def __unicode__(self):
        return self.eta_descripcion

class Formulario(models.Model):
    for_numero = models.IntegerField(primary_key=True,unique=True,verbose_name='Numero Formulario')
#    for_numero = models.AutoField(primary_key=True)
    res = models.ForeignKey('Responsable',verbose_name='Responsable')
    for_fecha = models.DateTimeField(null=True, blank=True,verbose_name='Fecha')
    class Meta:
        db_table = 'formulario'
    def __unicode__(self):
        return self.for_numero

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256)
    f_table_schema = models.CharField(max_length=256)
    f_table_name = models.CharField(max_length=256)
    f_geometry_column = models.CharField(max_length=256)
    coord_dimension = models.IntegerField()
    srid = models.IntegerField()
    type = models.CharField(max_length=30)
    class Meta:
        db_table = 'geometry_columns'

class Luminosidad(models.Model):
    lum_cod = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    lum_cod = models.AutoField(primary_key=True, unique=True)
    lum_descripcion = models.CharField(max_length=255, blank=True,verbose_name='Detalle')
    class Meta:
        db_table = 'luminosidad'
    def __unicode__(self):
        return self.lum_descripcion

class Maniobra(models.Model):
    man_cod = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    man_cod = models.AutoField(primary_key=True)
    man_descripcion = models.CharField(max_length=255, blank=True,verbose_name='Descripcion')
    class Meta:
        db_table = 'maniobra'
    def __unicode__(self):
        return self.man_descripcion

class Personas(models.Model):
    per_id = models.IntegerField(primary_key=True)
#    per_id = models.AutoField(primary_key=True)
    per_run = models.IntegerField()
    per_calidad = models.CharField(max_length=255, blank=True)
    per_genero = models.IntegerField(null=True, blank=True)
    per_edad = models.IntegerField(null=True, blank=True)
    per_resultado = models.CharField(max_length=255, blank=True)
    per_cinturon = models.IntegerField(null=True, blank=True)
    com_codigo2 = models.ForeignKey(Comuna2, db_column='com_codigo2')
    acc = models.ForeignKey(Accidente)
    veh_id2 = models.ForeignKey('Vehiculo2', db_column='veh_id2')
    veh_patente2 = models.CharField(max_length=20)
    per_licencia = models.CharField(max_length=3, blank=True)
    per_codigo = models.CharField(max_length=255, blank=True)
    per_condicion = models.IntegerField(null=True, blank=True)
    per_nacionalidad = models.CharField(max_length=100, blank=True)
    per_detenido = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'personas'
    def __unicode__(self):
        return self.per_run

class Region(models.Model):
    reg_codigo = models.IntegerField(primary_key=True,unique=True)
#    reg_codigo = models.AutoField(primary_key=True)
    reg_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'region'
    def __unicode__(self):
        return self.reg_nombre

class Responsable(models.Model):
    res_id = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    res_id = models.AutoField(primary_key=True)
    cmr_codigo = models.ForeignKey(Comisaria, db_column='cmr_codigo',verbose_name='Comisaria')
    res_nombre = models.CharField(max_length=255, blank=True,verbose_name='Nombre')
    res_grado = models.CharField(max_length=255, blank=True,verbose_name='Grado')
    class Meta:
        db_table = 'responsable'
    def __unicode__(self):
        return self.res_nombre

class Servicio(models.Model):
    ser_cod = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    ser_cod = models.AutoField(primary_key=True)
    ser_descripcion = models.CharField(max_length=255, blank=True,verbose_name='Descripcion')
    class Meta:
        db_table = 'servicio'
    def __unicode__(self):
        return self.ser_descripcion

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(null=True, blank=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)
    class Meta:
        db_table = 'spatial_ref_sys'

class SubSector(models.Model):
    sec_id = models.IntegerField(primary_key=True,unique=True)
#    sec_id = models.AutoField(primary_key=True)
    sec_descripcion = models.CharField(max_length=255, blank=True, verbose_name='subsector')
    class Meta:
        db_table = 'sub_sector'
    def __unicode_(self):
        return self.sec_descripcion

class TipoAccidente(models.Model):
    tac_id = models.IntegerField(primary_key=True,unique=True)
#    tac_id = models.AutoField(primary_key=True)
    tca_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'tipo_accidente'
    def __unicode__(self):
        return self.tca_descripcion

class TipoCalzada(models.Model):
    tca_cod = models.IntegerField(primary_key=True,unique=True)
#    tca_cod = models.AutoField(primary_key=True)
    tca_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'tipo_calzada'
    def __unicode__(self):
        return self.tca_descripcion

class TipoVehiculo(models.Model):
    tve_id = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    tve_id = models.AutoField(primary_key=True)
    tve_descripcion = models.CharField(max_length=255, blank=True,verbose_name='Descripcion')
    class Meta:
        db_table = 'tipo_vehiculo'
    def __unicode__(self):
        return self.tve_descripcion

class UbicacionRelativa(models.Model):
    ure_id = models.IntegerField(primary_key=True,unique=True,verbose_name='Codigo')
#    ure_id = models.AutoField(primary_key=True)
    dur_descripcion = models.CharField(max_length=255, blank=True,verbose_name='Descripcion')
    class Meta:
        db_table = 'ubicacion_relativa'
    def __unicode__(self):
        return self.dur_descripcion

class Vehiculo(models.Model):
    veh_id = models.IntegerField(primary_key=True,verbose_name='Codigo')
#    veh_id = models.AutoField(primary_key=True)
    veh_patente = models.CharField(max_length=20,verbose_name='Patente')
    tve = models.ForeignKey(TipoVehiculo,verbose_name='Tipo Vehiculo')
    #man_cod = models.ForeignKey(Maniobra, db_column='man_cod',verbose_name='Maniobra')
    ser_cod = models.ForeignKey(Servicio, db_column='ser_cod',verbose_name='Servicio')
    veh_concecuencia = models.CharField(max_length=255, blank=True,verbose_name='Consecuencia')
    veh_via = models.IntegerField(null=True,verbose_name='Via')
    veh_direccion = models.CharField(max_length=100, blank=True,verbose_name='Direccion')
    veh_marca = models.CharField(max_length=100, blank=True,verbose_name='Marca')
    veh_codigo = models.CharField(max_length=255, blank=True,verbose_name='Codigo')
    class Meta:
        db_table = 'vehiculo'
    def __unicode__(self):
        return self.veh_patente

class Vehiculo2(models.Model):
    veh_id2 = models.IntegerField(primary_key=True)
#    veh_id2 = models.AutoField(primary_key=True)
    veh_patente2 = models.CharField(max_length=20)
    veh_concecuencia = models.CharField(max_length=255, blank=True)
    veh_via = models.IntegerField(null=True, blank=True)
    veh_direccion = models.CharField(max_length=100, blank=True)
    veh_marca = models.CharField(max_length=100, blank=True)
    veh_codigo = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'vehiculo2'
    def __unicode__(self):
        return self.veh_patente2

