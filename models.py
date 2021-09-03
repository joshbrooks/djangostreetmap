from django.contrib.gis.db.models import GeometryField
from django.db import models


class PlanetOsmLine(models.Model):
    unique_id = models.BigIntegerField(primary_key=True)
    osm_id = models.BigIntegerField(blank=True, null=True)
    access = models.CharField(max_length=1024, blank=True, null=True)
    addr_housename = models.CharField(max_length=1024, db_column="addr:housename", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.CharField(max_length=1024, db_column="addr:housenumber", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.CharField(max_length=1024, db_column="addr:interpolation", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.CharField(max_length=1024, blank=True, null=True)
    aerialway = models.CharField(max_length=1024, blank=True, null=True)
    aeroway = models.CharField(max_length=1024, blank=True, null=True)
    amenity = models.CharField(max_length=1024, blank=True, null=True)
    barrier = models.CharField(max_length=1024, blank=True, null=True)
    bicycle = models.CharField(max_length=1024, blank=True, null=True)
    bridge = models.CharField(max_length=1024, blank=True, null=True)
    boundary = models.CharField(max_length=1024, blank=True, null=True)
    building = models.CharField(max_length=1024, blank=True, null=True)
    construction = models.CharField(max_length=1024, blank=True, null=True)
    covered = models.CharField(max_length=1024, blank=True, null=True)
    foot = models.CharField(max_length=1024, blank=True, null=True)
    highway = models.CharField(max_length=1024, blank=True, null=True)
    historic = models.CharField(max_length=1024, blank=True, null=True)
    horse = models.CharField(max_length=1024, blank=True, null=True)
    junction = models.CharField(max_length=1024, blank=True, null=True)
    landuse = models.CharField(max_length=1024, blank=True, null=True)
    layer = models.IntegerField(blank=True, null=True)
    leisure = models.CharField(max_length=1024, blank=True, null=True)
    lock = models.CharField(max_length=1024, blank=True, null=True)
    man_made = models.CharField(max_length=1024, blank=True, null=True)
    military = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    natural = models.CharField(max_length=1024, blank=True, null=True)
    oneway = models.CharField(max_length=1024, blank=True, null=True)
    place = models.CharField(max_length=1024, blank=True, null=True)
    power = models.CharField(max_length=1024, blank=True, null=True)
    railway = models.CharField(max_length=1024, blank=True, null=True)
    ref = models.CharField(max_length=1024, blank=True, null=True)
    religion = models.CharField(max_length=1024, blank=True, null=True)
    route = models.CharField(max_length=1024, blank=True, null=True)
    service = models.CharField(max_length=1024, blank=True, null=True)
    shop = models.CharField(max_length=1024, blank=True, null=True)
    surface = models.CharField(max_length=1024, blank=True, null=True)
    tourism = models.CharField(max_length=1024, blank=True, null=True)
    tracktype = models.CharField(max_length=1024, blank=True, null=True)
    tunnel = models.CharField(max_length=1024, blank=True, null=True)
    water = models.CharField(max_length=1024, blank=True, null=True)
    waterway = models.CharField(max_length=1024, blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way = GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "planet_osm_line"


class PlanetOsmPoint(models.Model):
    unique_id = models.BigIntegerField(primary_key=True)
    osm_id = models.BigIntegerField(blank=True, null=True)
    access = models.CharField(max_length=1024, blank=True, null=True)
    addr_housename = models.CharField(max_length=1024, db_column="addr:housename", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.CharField(max_length=1024, db_column="addr:housenumber", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.CharField(max_length=1024, blank=True, null=True)
    aerialway = models.CharField(max_length=1024, blank=True, null=True)
    aeroway = models.CharField(max_length=1024, blank=True, null=True)
    amenity = models.CharField(max_length=1024, blank=True, null=True)
    barrier = models.CharField(max_length=1024, blank=True, null=True)
    boundary = models.CharField(max_length=1024, blank=True, null=True)
    building = models.CharField(max_length=1024, blank=True, null=True)
    highway = models.CharField(max_length=1024, blank=True, null=True)
    historic = models.CharField(max_length=1024, blank=True, null=True)
    junction = models.CharField(max_length=1024, blank=True, null=True)
    landuse = models.CharField(max_length=1024, blank=True, null=True)
    layer = models.IntegerField(blank=True, null=True)
    leisure = models.CharField(max_length=1024, blank=True, null=True)
    lock = models.CharField(max_length=1024, blank=True, null=True)
    man_made = models.CharField(max_length=1024, blank=True, null=True)
    military = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    natural = models.CharField(max_length=1024, blank=True, null=True)
    oneway = models.CharField(max_length=1024, blank=True, null=True)
    place = models.CharField(max_length=1024, blank=True, null=True)
    power = models.CharField(max_length=1024, blank=True, null=True)
    railway = models.CharField(max_length=1024, blank=True, null=True)
    ref = models.CharField(max_length=1024, blank=True, null=True)
    religion = models.CharField(max_length=1024, blank=True, null=True)
    shop = models.CharField(max_length=1024, blank=True, null=True)
    tourism = models.CharField(max_length=1024, blank=True, null=True)
    water = models.CharField(max_length=1024, blank=True, null=True)
    waterway = models.CharField(max_length=1024, blank=True, null=True)
    way = GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "planet_osm_point"


class PlanetOsmPolygon(models.Model):
    unique_id = models.BigIntegerField(primary_key=True)
    osm_id = models.BigIntegerField(blank=True, null=True)
    access = models.CharField(max_length=1024, blank=True, null=True)
    addr_housename = models.CharField(max_length=1024, db_column="addr:housename", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.CharField(max_length=1024, db_column="addr:housenumber", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.CharField(max_length=1024, db_column="addr:interpolation", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.CharField(max_length=1024, blank=True, null=True)
    aerialway = models.CharField(max_length=1024, blank=True, null=True)
    aeroway = models.CharField(max_length=1024, blank=True, null=True)
    amenity = models.CharField(max_length=1024, blank=True, null=True)
    barrier = models.CharField(max_length=1024, blank=True, null=True)
    bicycle = models.CharField(max_length=1024, blank=True, null=True)
    bridge = models.CharField(max_length=1024, blank=True, null=True)
    boundary = models.CharField(max_length=1024, blank=True, null=True)
    building = models.CharField(max_length=1024, blank=True, null=True)
    construction = models.CharField(max_length=1024, blank=True, null=True)
    covered = models.CharField(max_length=1024, blank=True, null=True)
    foot = models.CharField(max_length=1024, blank=True, null=True)
    highway = models.CharField(max_length=1024, blank=True, null=True)
    historic = models.CharField(max_length=1024, blank=True, null=True)
    horse = models.CharField(max_length=1024, blank=True, null=True)
    junction = models.CharField(max_length=1024, blank=True, null=True)
    landuse = models.CharField(max_length=1024, blank=True, null=True)
    layer = models.IntegerField(blank=True, null=True)
    leisure = models.CharField(max_length=1024, blank=True, null=True)
    lock = models.CharField(max_length=1024, blank=True, null=True)
    man_made = models.CharField(max_length=1024, blank=True, null=True)
    military = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    natural = models.CharField(max_length=1024, blank=True, null=True)
    oneway = models.CharField(max_length=1024, blank=True, null=True)
    place = models.CharField(max_length=1024, blank=True, null=True)
    power = models.CharField(max_length=1024, blank=True, null=True)
    railway = models.CharField(max_length=1024, blank=True, null=True)
    ref = models.CharField(max_length=1024, blank=True, null=True)
    religion = models.CharField(max_length=1024, blank=True, null=True)
    route = models.CharField(max_length=1024, blank=True, null=True)
    service = models.CharField(max_length=1024, blank=True, null=True)
    shop = models.CharField(max_length=1024, blank=True, null=True)
    surface = models.CharField(max_length=1024, blank=True, null=True)
    tourism = models.CharField(max_length=1024, blank=True, null=True)
    tracktype = models.CharField(max_length=1024, blank=True, null=True)
    tunnel = models.CharField(max_length=1024, blank=True, null=True)
    water = models.CharField(max_length=1024, blank=True, null=True)
    waterway = models.CharField(max_length=1024, blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way = GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "planet_osm_polygon"


class HighwaysManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(highway__isnull=False)


class PlanetOsmRoads(PlanetOsmLine):
    """
    The default "planet osm roads" layer is a bit iffy
    This uses a custom manager to generate roads instead
    """

    class Meta:
        proxy = True

    objects = HighwaysManager()
