from django.contrib import admin

try:
    from django.contrib.gis.forms.widgets import OSMWidget
except ImportError:
    from django.contrib.gis.admin import OSMWidget  # type: ignore

from djangostreetmap import models


@admin.register(models.SimplifiedLandPolygon)
class SimplifiedLandPolygonAdmin(admin.ModelAdmin):  # type: ignore
    formfield_overrides = {
        models.MultiPolygonField: {"widget": OSMWidget},
    }
