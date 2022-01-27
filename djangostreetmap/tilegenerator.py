from dataclasses import dataclass, field
from typing import List, Sequence

from psycopg2 import sql

from django.db import connection

# To time mvt queries uncomment the following
# from .timer import Timer


@dataclass
class Tile:
    """
    Simple dataclass representing a "tile" instance and additional metadata
    for tile generation: buffer, extent and margin
    http://postgis.net/docs/ST_TileEnvelope.html

    """

    zoom: int
    x: int
    y: int
    buffer: int = 64
    extent: int = 4096

    @staticmethod
    def tile_envelope() -> sql.Composable:
        return sql.SQL("ST_TileEnvelope(%(zoom)s, %(x)s, %(y)s)")

    @staticmethod
    def tile_envelope_margin() -> sql.Composable:
        return sql.SQL("ST_TileEnvelope(%(zoom)s, %(x)s, %(y)s, margin => (%(buffer)s / %(extent)s))")


@dataclass
class MvtQuery:
    """
    This is a SQL query generator based on the example
    at https://postgis.net/docs/manual-dev/ST_AsMVT.html
    """

    table: str
    attributes: List[str] = field(default_factory=list)
    filters: Sequence[sql.Composable] = field(default_factory=list)
    transform: bool = False  # Set to True if source srid is not 3857, but beware performance
    field: str = "geom"
    pk: str = "id"
    layer: str = "default"
    centroid: bool = False

    @property
    def json_attributes(self) -> sql.Composed:
        """
        Create a "JSONB_BUILD_OBJECT" clause
        """
        if not self.attributes:
            return sql.SQL("")
        params = None
        for a in self.attributes:
            if not params:
                params = sql.Literal(a)
            else:
                params += sql.Literal(a)  # Name of the key is the same as the field
            params += sql.Identifier(a)  # The field to use as the value for the JSON
        composed_params = params.join(", ")  # type: ignore
        return sql.SQL(", jsonb_build_object({})").format(composed_params)

    @property
    def transformed_geom(self) -> sql.Composable:
        """
        Return an `ST_TRANSFORM` clause
        https://postgis.net/docs/ST_Transform.html
        """
        template = "{field}"
        if self.transform:
            template = f"ST_TRANSFORM({template}, 3857)"
        return sql.SQL(template).format(field=sql.Identifier(self.field))

    @property
    def centroid_wrap(self) -> sql.Composable:
        if self.centroid:
            return sql.SQL("ST_CENTROID({})").format(self.transformed_geom)
        return self.transformed_geom

    @property
    def alias(self) -> sql.Composable:
        """
        The name of the query alias to use for postgresql
        """
        return sql.Identifier(f"mvt_{self.layer}")

    @property
    def where(self) -> sql.Composable:
        if self.filters:
            where_clause = sql.SQL(" AND ") + sql.SQL(" AND ").join([self.filters])
        else:
            where_clause = sql.SQL("")
        return where_clause

    @property
    def as_mvtgeom(self) -> sql.Composable:

        return sql.SQL(
            """
            ST_AsMVTGeom(
                {cg},
                {e},
                extent => %(extent)s,
                buffer => %(buffer)s
            ) AS geom, {pk} {json_attributes}
            FROM {t}
            WHERE {g} && {m} {where}
            """
        ).format(
            cg=self.centroid_wrap,
            g=self.transformed_geom,
            m=Tile.tile_envelope_margin(),
            e=Tile.tile_envelope(),
            t=sql.Identifier(self.table),
            # Properties of "self"
            pk=sql.Identifier(self.pk),
            json_attributes=self.json_attributes,
            where=self.where,
        )

    def as_mvt(self) -> sql.Composed:
        outer_query = sql.SQL("""WITH {alias} AS (SELECT {inner_query} ) SELECT ST_AsMVT( {alias}.*, {layer}, %(extent)s, 'geom', {pk}) FROM {alias}""")
        parameters = dict(alias=self.alias, layer=sql.Literal(self.layer), inner_query=self.as_mvtgeom, pk=sql.Literal(self.pk))
        return outer_query.format(**parameters)

    def debug(self) -> str:
        with connection.cursor() as cursor:
            return self.as_mvt().as_string(cursor.cursor)
