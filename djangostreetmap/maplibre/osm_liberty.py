from maplibre.layer import Layer as L

layers = [L(type="background", id="background", paint={"background-color": "rgb(239,239,239)"})]

L(id="natural_earth", type="raster", source="natural_earth_shaded_relief", maxzoom=6, paint={"raster-opacity": {"base": 1.5, "stops": [[0, 0.6], [6, 0.1]]}})

L(id="park", type="fill", source="openmaptiles", sourceLayer="park", paint={"fill-color": "#d8e8c8", "fill-opacity": 0.7, "fill-outline-color": "rgba(95, 208, 100, 1)"})

L(id="park_outline", type="line", source="openmaptiles", sourceLayer="park", paint={"line-dasharray": [1, 1.5], "line-color": "rgba(228, 241, 215, 1)"})

L(
    id="landuse_residential",
    type="fill",
    source="openmaptiles",
    sourceLayer="landuse",
    maxzoom=8,
    filter=["==", "class", "residential"],
    paint={"fill-color": {"base": 1, "stops": [[9, "hsla(0, 3%, 85%, 0.84)"], [12, "hsla(35, 57%, 88%, 0.49)"]]}},
)

L(
    id="landcover_wood",
    type="fill",
    source="openmaptiles",
    sourceLayer="landcover",
    filter=["all", ["==", "class", "wood"]],
    paint={"fill-antialias": False, "fill-color": "hsla(98, 61%, 72%, 0.7)", "fill-opacity": 0.4},
)

L(
    id="landcover_grass",
    type="fill",
    source="openmaptiles",
    sourceLayer="landcover",
    filter=["all", ["==", "class", "grass"]],
    paint={"fill-antialias": False, "fill-color": "rgba(176, 213, 154, 1)", "fill-opacity": 0.3},
)

L(
    id="landcover_ice",
    type="fill",
    source="openmaptiles",
    sourceLayer="landcover",
    filter=["all", ["==", "class", "ice"]],
    paint={"fill-antialias": False, "fill-color": "rgba(224, 236, 236, 1)", "fill-opacity": 0.8},
)

L(id="landuse_cemetery", type="fill", source="openmaptiles", sourceLayer="landuse", filter=["==", "class", "cemetery"], paint={"fill-color": "hsl(75, 37%, 81%)"})

L(id="landuse_hospital", type="fill", source="openmaptiles", sourceLayer="landuse", filter=["==", "class", "hospital"], paint={"fill-color": "#fde"})

L(id="landuse_school", type="fill", source="openmaptiles", sourceLayer="landuse", filter=["==", "class", "school"], paint={"fill-color": "rgb(236,238,204)"})

L(
    id="waterway_tunnel",
    type="line",
    source="openmaptiles",
    sourceLayer="waterway",
    filter=["all", ["==", "brunnel", "tunnel"]],
    paint={
        "line-color": "#a0c8f0",
        "line-dasharray": [3, 3],
        "line-gap-width": {"stops": [[12, 0], [20, 6]]},
        "line-opacity": 1,
        "line-width": {"base": 1.4, "stops": [[8, 1], [20, 2]]},
    },
)

L(
    id="waterway_river",
    type="line",
    source="openmaptiles",
    sourceLayer="waterway",
    filter=["all", ["==", "class", "river"], ["!=", "brunnel", "tunnel"]],
    layout={"line-cap": "round"},
    paint={"line-color": "#a0c8f0", "line-width": {"base": 1.2, "stops": [[11, 0.5], [20, 6]]}},
)

L(
    id="waterway_other",
    type="line",
    source="openmaptiles",
    sourceLayer="waterway",
    filter=["all", ["!=", "class", "river"], ["!=", "brunnel", "tunnel"]],
    layout={"line-cap": "round"},
    paint={"line-color": "#a0c8f0", "line-width": {"base": 1.3, "stops": [[13, 0.5], [20, 6]]}},
)

L(id="water", type="fill", source="openmaptiles", sourceLayer="water", filter=["all", ["!=", "brunnel", "tunnel"]], paint={"fill-color": "rgb(158,189,255)"})

L(id="landcover_sand", type="fill", source="openmaptiles", sourceLayer="landcover", filter=["all", ["==", "class", "sand"]], paint={"fill-color": "rgba(247, 239, 195, 1)"})

L(
    id="aeroway_fill",
    type="fill",
    source="openmaptiles",
    sourceLayer="aeroway",
    minzoom=11,
    filter=["==", "$type", "Polygon"],
    paint={"fill-color": "rgba(229, 228, 224, 1)", "fill-opacity": 0.7},
)

L(
    id="aeroway_runway",
    type="line",
    source="openmaptiles",
    sourceLayer="aeroway",
    minzoom=11,
    filter=["all", ["==", "$type", "LineString"], ["==", "class", "runway"]],
    paint={"line-color": "#f0ede9", "line-width": {"base": 1.2, "stops": [[11, 3], [20, 16]]}},
)

L(
    id="aeroway_taxiway",
    type="line",
    source="openmaptiles",
    sourceLayer="aeroway",
    minzoom=11,
    filter=["all", ["==", "$type", "LineString"], ["==", "class", "taxiway"]],
    paint={"line-color": "#f0ede9", "line-width": {"base": 1.2, "stops": [[11, 0.5], [20, 6]]}},
)

L(
    id="tunnel_motorway_link_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["==", "ramp", 1], ["==", "brunnel", "tunnel"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-dasharray": [0.5, 0.25], "line-width": {"base": 1.2, "stops": [[12, 1], [13, 3], [14, 4], [20, 15]]}},
)

L(
    id="tunnel_service_track_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "service", "track"]],
    layout={"line-join": "round"},
    paint={"line-color": "#cfcdca", "line-dasharray": [0.5, 0.25], "line-width": {"base": 1.2, "stops": [[15, 1], [16, 4], [20, 11]]}},
)

L(
    id="tunnel_link_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "ramp", 1], ["==", "brunnel", "tunnel"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[12, 1], [13, 3], [14, 4], [20, 15]]}},
)

L(
    id="tunnel_street_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "street", "street_limited"]],
    layout={"line-join": "round"},
    paint={"line-color": "#cfcdca", "line-opacity": {"stops": [[12, 0], [12.5, 1]]}, "line-width": {"base": 1.2, "stops": [[12, 0.5], [13, 1], [14, 4], [20, 15]]}},
)


L(
    id="tunnel_secondary_tertiary_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "secondary", "tertiary"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[8, 1.5], [20, 17]]}},
)

L(
    id="tunnel_trunk_primary_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "primary", "trunk"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[5, 0.4], [6, 0.7], [7, 1.75], [20, 22]]}},
)


L(
    id="tunnel_motorway_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["!=", "ramp", 1], ["==", "brunnel", "tunnel"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-dasharray": [0.5, 0.25], "line-width": {"base": 1.2, "stops": [[5, 0.4], [6, 0.7], [7, 1.75], [20, 22]]}},
)


L(
    id="tunnel_path_pedestrian",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "$type", "LineString"], ["==", "brunnel", "tunnel"], ["in", "class", "path", "pedestrian"]],
    paint={"line-color": "hsl(0, 0%, 100%)", "line-dasharray": [1, 0.75], "line-width": {"base": 1.2, "stops": [[14, 0.5], [20, 10]]}},
)

L(
    id="tunnel_motorway_link",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["==", "ramp", 1], ["==", "brunnel", "tunnel"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fc8", "line-width": {"base": 1.2, "stops": [[12.5, 0], [13, 1.5], [14, 2.5], [20, 11.5]]}},
)


L(
    id="tunnel_service_track",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "service", "track"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff", "line-width": {"base": 1.2, "stops": [[15.5, 0], [16, 2], [20, 7.5]]}},
)

L(
    id="tunnel_link",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "ramp", 1], ["==", "brunnel", "tunnel"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff4c6", "line-width": {"base": 1.2, "stops": [[12.5, 0], [13, 1.5], [14, 2.5], [20, 11.5]]}},
)


L(
    id="tunnel_minor",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "minor"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff", "line-width": {"base": 1.2, "stops": [[13.5, 0], [14, 2.5], [20, 11.5]]}},
)

L(
    id="tunnel_secondary_tertiary",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "secondary", "tertiary"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff4c6", "line-width": {"base": 1.2, "stops": [[6.5, 0], [7, 0.5], [20, 10]]}},
)

L(
    id="tunnel_trunk_primary",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "primary", "trunk"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff4c6", "line-width": {"base": 1.2, "stops": [[5, 0], [7, 1], [20, 18]]}},
)

L(
    id="tunnel_motorway",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["!=", "ramp", 1], ["==", "brunnel", "tunnel"]],
    layout={"line-join": "round"},
    paint={"line-color": "#ffdaa6", "line-width": {"base": 1.2, "stops": [[5, 0], [7, 1], [20, 18]]}},
)

L(
    id="tunnel_major_rail",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "rail"]],
    paint={"line-color": "#bbb", "line-width": {"base": 1.4, "stops": [[14, 0.4], [15, 0.75], [20, 2]]}},
)

L(
    id="tunnel_major_rail_hatching",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["==", "class", "rail"]],
    paint={"line-color": "#bbb", "line-dasharray": [0.2, 8], "line-width": {"base": 1.4, "stops": [[14.5, 0], [15, 3], [20, 8]]}},
)

L(
    id="tunnel_transit_rail",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["in", "class", "transit"]],
    paint={"line-color": "#bbb", "line-width": {"base": 1.4, "stops": [[14, 0.4], [15, 0.75], [20, 2]]}},
)

L(
    id="tunnel_transit_rail_hatching",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "tunnel"], ["==", "class", "transit"]],
    paint={"line-color": "#bbb", "line-dasharray": [0.2, 8], "line-width": {"base": 1.4, "stops": [[14.5, 0], [15, 3], [20, 8]]}},
)

L(
    id="road_area_pattern",
    type="fill",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "$type", "Polygon"]],
    paint={"fill-pattern": "pedestrian_polygon"},
)

L(
    id="road_motorway_link_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=12,
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "motorway"], ["==", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[12, 1], [13, 3], [14, 4], [20, 15]]}},
)


L(
    id="road_service_track_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "service", "track"]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#cfcdca", "line-width": {"base": 1.2, "stops": [[15, 1], [16, 4], [20, 11]]}},
)

L(
    id="road_link_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=13,
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["!in", "class", "pedestrian", "path", "track", "service", "motorway"], ["==", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[12, 1], [13, 3], [14, 4], [20, 15]]}},
)


L(
    id="road_minor_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "$type", "LineString"], ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "minor"], ["!=", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#cfcdca", "line-opacity": {"stops": [[12, 0], [12.5, 1]]}, "line-width": {"base": 1.2, "stops": [[12, 0.5], [13, 1], [14, 4], [20, 20]]}},
)

L(
    id="road_secondary_tertiary_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "secondary", "tertiary"], ["!=", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[8, 1.5], [20, 17]]}},
)

L(
    id="road_trunk_primary_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "primary", "trunk"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[5, 0.4], [6, 0.7], [7, 1.75], [20, 22]]}},
)


L(
    id="road_motorway_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=5,
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "motorway"], ["!=", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[5, 0.4], [6, 0.7], [7, 1.75], [20, 22]]}},
)


L(
    id="road_path_pedestrian",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=14,
    filter=["all", ["==", "$type", "LineString"], ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "path", "pedestrian"]],
    layout={"line-join": "round"},
    paint={"line-color": "hsl(0, 0%, 100%)", "line-dasharray": [1, 0.7], "line-width": {"base": 1.2, "stops": [[14, 1], [20, 10]]}},
)

L(
    id="road_motorway_link",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=12,
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "motorway"], ["==", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#fc8", "line-width": {"base": 1.2, "stops": [[12.5, 0], [13, 1.5], [14, 2.5], [20, 11.5]]}},
)


L(
    id="road_service_track",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "service", "track"]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#fff", "line-width": {"base": 1.2, "stops": [[15.5, 0], [16, 2], [20, 7.5]]}},
)

L(
    id="road_link",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=13,
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "ramp", 1], ["!in", "class", "pedestrian", "path", "track", "service", "motorway"]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#fea", "line-width": {"base": 1.2, "stops": [[12.5, 0], [13, 1.5], [14, 2.5], [20, 11.5]]}},
)

L(
    id="road_minor",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "$type", "LineString"], ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "minor"]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#fff", "line-width": {"base": 1.2, "stops": [[13.5, 0], [14, 2.5], [20, 18]]}},
)

L(
    id="road_secondary_tertiary",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "secondary", "tertiary"]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "#fea", "line-width": {"base": 1.2, "stops": [[6.5, 0], [8, 0.5], [20, 13]]}},
)

L(
    id="road_trunk_primary",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["in", "class", "primary", "trunk"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fea", "line-width": {"base": 1.2, "stops": [[5, 0], [7, 1], [20, 18]]}},
)

L(
    id="road_motorway",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=5,
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "motorway"], ["!=", "ramp", 1]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": {"base": 1, "stops": [[5, "hsl(26, 87%, 62%)"], [6, "#fc8"]]}, "line-width": {"base": 1.2, "stops": [[5, 0], [7, 1], [20, 18]]}},
)


L(
    id="road_major_rail",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "rail"]],
    paint={"line-color": "#bbb", "line-width": {"base": 1.4, "stops": [[14, 0.4], [15, 0.75], [20, 2]]}},
)

L(
    id="road_major_rail_hatching",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "rail"]],
    paint={"line-color": "#bbb", "line-dasharray": [0.2, 8], "line-width": {"base": 1.4, "stops": [[14.5, 0], [15, 3], [20, 8]]}},
)

L(
    id="road_transit_rail",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "transit"]],
    paint={"line-color": "#bbb", "line-width": {"base": 1.4, "stops": [[14, 0.4], [15, 0.75], [20, 2]]}},
)

L(
    id="road_transit_rail_hatching",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["!in", "brunnel", "bridge", "tunnel"], ["==", "class", "transit"]],
    paint={"line-color": "#bbb", "line-dasharray": [0.2, 8], "line-width": {"base": 1.4, "stops": [[14.5, 0], [15, 3], [20, 8]]}},
)

L(
    id="road_one_way_arrow",
    type="symbol",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=15,
    filter=["==", "oneway", 1],
    layout={"icon-image": "arrow", "symbol-placement": "line"},
)

L(
    id="road_one_way_arrow_opposite",
    type="symbol",
    source="openmaptiles",
    sourceLayer="transportation",
    minzoom=15,
    filter=["==", "oneway", -1],
    layout={"icon-image": "arrow", "symbol-placement": "line", "icon-rotate": 180},
)

L(
    id="bridge_motorway_link_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["==", "ramp", 1], ["==", "brunnel", "bridge"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[12, 1], [13, 3], [14, 4], [20, 15]]}},
)


L(
    id="bridge_service_track_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "service", "track"]],
    layout={"line-join": "round"},
    paint={"line-color": "#cfcdca", "line-width": {"base": 1.2, "stops": [[15, 1], [16, 4], [20, 11]]}},
)

L(
    id="bridge_link_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "link"], ["==", "brunnel", "bridge"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[12, 1], [13, 3], [14, 4], [20, 15]]}},
)

L(
    id="bridge_street_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "street", "street_limited"]],
    layout={"line-join": "round"},
    paint={"line-color": "hsl(36, 6%, 74%)", "line-opacity": {"stops": [[12, 0], [12.5, 1]]}, "line-width": {"base": 1.2, "stops": [[12, 0.5], [13, 1], [14, 4], [20, 25]]}},
)


L(
    id="bridge_path_pedestrian_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "$type", "LineString"], ["==", "brunnel", "bridge"], ["in", "class", "path", "pedestrian"]],
    paint={"line-color": "hsl(35, 6%, 80%)", "line-dasharray": [1, 0], "line-width": {"base": 1.2, "stops": [[14, 1.5], [20, 18]]}},
)

L(
    id="bridge_secondary_tertiary_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "secondary", "tertiary"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[8, 1.5], [20, 17]]}},
)

L(
    id="bridge_trunk_primary_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "primary", "trunk"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[5, 0.4], [6, 0.7], [7, 1.75], [20, 22]]}},
)


L(
    id="bridge_motorway_casing",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["!=", "ramp", 1], ["==", "brunnel", "bridge"]],
    layout={"line-join": "round"},
    paint={"line-color": "#e9ac77", "line-width": {"base": 1.2, "stops": [[5, 0.4], [6, 0.7], [7, 1.75], [20, 22]]}},
)


L(
    id="bridge_path_pedestrian",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "$type", "LineString"], ["==", "brunnel", "bridge"], ["in", "class", "path", "pedestrian"]],
    paint={"line-color": "hsl(0, 0%, 100%)", "line-dasharray": [1, 0.3], "line-width": {"base": 1.2, "stops": [[14, 0.5], [20, 10]]}},
)

L(
    id="bridge_motorway_link",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["==", "ramp", 1], ["==", "brunnel", "bridge"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fc8", "line-width": {"base": 1.2, "stops": [[12.5, 0], [13, 1.5], [14, 2.5], [20, 11.5]]}},
)


L(
    id="bridge_service_track",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "service", "track"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff", "line-width": {"base": 1.2, "stops": [[15.5, 0], [16, 2], [20, 7.5]]}},
)

L(
    id="bridge_link",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "link"], ["==", "brunnel", "bridge"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fea", "line-width": {"base": 1.2, "stops": [[12.5, 0], [13, 1.5], [14, 2.5], [20, 11.5]]}},
)


L(
    id="bridge_street",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "minor"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fff", "line-width": {"base": 1.2, "stops": [[13.5, 0], [14, 2.5], [20, 18]]}},
)

L(
    id="bridge_secondary_tertiary",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "secondary", "tertiary"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fea", "line-width": {"base": 1.2, "stops": [[6.5, 0], [7, 0.5], [20, 10]]}},
)

L(
    id="bridge_trunk_primary",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "brunnel", "bridge"], ["in", "class", "primary", "trunk"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fea", "line-width": {"base": 1.2, "stops": [[5, 0], [7, 1], [20, 18]]}},
)

L(
    id="bridge_motorway",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "motorway"], ["!=", "ramp", 1], ["==", "brunnel", "bridge"]],
    layout={"line-join": "round"},
    paint={"line-color": "#fc8", "line-width": {"base": 1.2, "stops": [[5, 0], [7, 1], [20, 18]]}},
)

L(
    id="bridge_major_rail",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "rail"], ["==", "brunnel", "bridge"]],
    paint={"line-color": "#bbb", "line-width": {"base": 1.4, "stops": [[14, 0.4], [15, 0.75], [20, 2]]}},
)

L(
    id="bridge_major_rail_hatching",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "rail"], ["==", "brunnel", "bridge"]],
    paint={"line-color": "#bbb", "line-dasharray": [0.2, 8], "line-width": {"base": 1.4, "stops": [[14.5, 0], [15, 3], [20, 8]]}},
)

L(
    id="bridge_transit_rail",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "transit"], ["==", "brunnel", "bridge"]],
    paint={"line-color": "#bbb", "line-width": {"base": 1.4, "stops": [[14, 0.4], [15, 0.75], [20, 2]]}},
)

L(
    id="bridge_transit_rail_hatching",
    type="line",
    source="openmaptiles",
    sourceLayer="transportation",
    filter=["all", ["==", "class", "transit"], ["==", "brunnel", "bridge"]],
    paint={"line-color": "#bbb", "line-dasharray": [0.2, 8], "line-width": {"base": 1.4, "stops": [[14.5, 0], [15, 3], [20, 8]]}},
)

L(
    id="building",
    type="fill",
    source="openmaptiles",
    sourceLayer="building",
    minzoom=13,
    maxzoom=14,
    paint={"fill-color": "hsl(35, 8%, 85%)", "fill-outline-color": {"base": 1, "stops": [[13, "hsla(35, 6%, 79%, 0.32)"], [14, "hsl(35, 6%, 79%)"]]}},
)


L(
    id="building-3d",
    type="fill-extrusion",
    source="openmaptiles",
    sourceLayer="building",
    minzoom=14,
    paint={
        "fill-extrusion-color": "hsl(35, 8%, 85%)",
        "fill-extrusion-height": {"property": "render_height", "type": "identity"},
        "fill-extrusion-base": {"property": "render_min_height", "type": "identity"},
        "fill-extrusion-opacity": 0.8,
    },
)


L(
    id="boundary_3",
    type="line",
    source="openmaptiles",
    sourceLayer="boundary",
    minzoom=8,
    filter=["all", ["in", "admin_level", 3, 4]],
    layout={"line-join": "round"},
    paint={"line-color": "#9e9cab", "line-dasharray": [5, 1], "line-width": {"base": 1, "stops": [[4, 0.4], [5, 1], [12, 1.8]]}},
)

L(
    id="boundary_2_z0-4",
    type="line",
    source="openmaptiles",
    sourceLayer="boundary",
    maxzoom=5,
    filter=["all", ["==", "admin_level", 2], ["!has", "claimed_by"]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "hsl(248, 1%, 41%)", "line-opacity": {"base": 1, "stops": [[0, 0.4], [4, 1]]}, "line-width": {"base": 1, "stops": [[3, 1], [5, 1.2], [12, 3]]}},
)

L(
    id="boundary_2_z5-",
    type="line",
    source="openmaptiles",
    sourceLayer="boundary",
    minzoom=5,
    filter=["all", ["==", "admin_level", 2]],
    layout={"line-cap": "round", "line-join": "round"},
    paint={"line-color": "hsl(248, 1%, 41%)", "line-opacity": {"base": 1, "stops": [[0, 0.4], [4, 1]]}, "line-width": {"base": 1, "stops": [[3, 1], [5, 1.2], [12, 3]]}},
)

L(
    id="water_name_line",
    type="symbol",
    source="openmaptiles",
    sourceLayer="waterway",
    filter=["all", ["==", "$type", "LineString"]],
    layout={"text-field": "{name}", "text-font": ["Roboto Regular"], "text-max-width": 5, "text-size": 12, "symbol-placement": "line"},
    paint={"text-color": "#5d60be", "text-halo-color": "rgba(255,255,255,0.7)", "text-halo-width": 1},
)

L(
    id="water_name_point",
    type="symbol",
    source="openmaptiles",
    sourceLayer="water_name",
    filter=["==", "$type", "Point"],
    layout={"text-field": "{name}", "text-font": ["Roboto Regular"], "text-max-width": 5, "text-size": 12},
    paint={"text-color": "#5d60be", "text-halo-color": "rgba(255,255,255,0.7)", "text-halo-width": 1},
)

L(
    id="poi_z16",
    type="symbol",
    source="openmaptiles",
    sourceLayer="poi",
    minzoom=16,
    filter=["all", ["==", "$type", "Point"], [">=", "rank", 20]],
    layout={
        "icon-image": "{class}_11",
        "text-anchor": "top",
        "text-field": "{name}",
        "text-font": ["Roboto Condensed Italic"],
        "text-max-width": 9,
        "text-offset": [0, 0.6],
        "text-size": 12,
    },
    paint={"text-color": "#666", "text-halo-blur": 0.5, "text-halo-color": "#ffffff", "text-halo-width": 1},
)

L(
    id="poi_z15",
    type="symbol",
    source="openmaptiles",
    sourceLayer="poi",
    minzoom=15,
    filter=["all", ["==", "$type", "Point"], [">=", "rank", 7], ["<", "rank", 20]],
    layout={
        "icon-image": "{class}_11",
        "text-anchor": "top",
        "text-field": "{name}",
        "text-font": ["Roboto Condensed Italic"],
        "text-max-width": 9,
        "text-offset": [0, 0.6],
        "text-size": 12,
    },
    paint={"text-color": "#666", "text-halo-blur": 0.5, "text-halo-color": "#ffffff", "text-halo-width": 1},
)

L(
    id="poi_z14",
    type="symbol",
    source="openmaptiles",
    sourceLayer="poi",
    minzoom=14,
    filter=["all", ["==", "$type", "Point"], [">=", "rank", 1], ["<", "rank", 7]],
    layout={
        "icon-image": "{class}_11",
        "text-anchor": "top",
        "text-field": "{name}",
        "text-font": ["Roboto Condensed Italic"],
        "text-max-width": 9,
        "text-offset": [0, 0.6],
        "text-size": 12,
    },
    paint={"text-color": "#666", "text-halo-blur": 0.5, "text-halo-color": "#ffffff", "text-halo-width": 1},
)

L(
    id="poi_transit",
    type="symbol",
    source="openmaptiles",
    sourceLayer="poi",
    filter=["all", ["in", "class", "bus", "rail", "airport"]],
    layout={
        "icon-image": "{class}_11",
        "text-anchor": "left",
        "text-field": "{name_en}",
        "text-font": ["Roboto Condensed Italic"],
        "text-max-width": 9,
        "text-offset": [0.9, 0],
        "text-size": 12,
    },
    paint={"text-color": "#4898ff", "text-halo-blur": 0.5, "text-halo-color": "#ffffff", "text-halo-width": 1},
)

L(
    id="road_label",
    type="symbol",
    source="openmaptiles",
    sourceLayer="transportation_name",
    filter=["all"],
    layout={
        "symbol-placement": "line",
        "text-anchor": "center",
        "text-field": "{name}",
        "text-font": ["Roboto Regular"],
        "text-offset": [0, 0.15],
        "text-size": {"base": 1, "stops": [[13, 12], [14, 13]]},
    },
    paint={"text-color": "#765", "text-halo-blur": 0.5, "text-halo-width": 1},
)

L(
    id="road_shield",
    type="symbol",
    source="openmaptiles",
    sourceLayer="transportation_name",
    minzoom=7,
    filter=["all", ["<=", "ref_length", 6]],
    layout={
        "icon-image": "default_{ref_length}",
        "icon-rotation-alignment": "viewport",
        "symbol-placement": {"base": 1, "stops": [[10, "point"], [11, "line"]]},
        "symbol-spacing": 500,
        "text-field": "{ref}",
        "text-font": ["Roboto Regular"],
        "text-offset": [0, 0.1],
        "text-rotation-alignment": "viewport",
        "text-size": 10,
        "icon-size": 0.8,
    },
)

L(
    id="place_other",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    filter=["all", ["in", "class", "hamlet", "island", "islet", "neighbourhood", "suburb", "quarter"]],
    layout={
        "text-field": "{name_en}",
        "text-font": ["Roboto Condensed Italic"],
        "text-letter-spacing": 0.1,
        "text-max-width": 9,
        "text-size": {"base": 1.2, "stops": [[12, 10], [15, 14]]},
        "text-transform": "uppercase",
    },
    paint={"text-color": "#633", "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1.2},
)

L(
    id="place_village",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    filter=["all", ["==", "class", "village"]],
    layout={"text-field": "{name_en}", "text-font": ["Roboto Regular"], "text-max-width": 8, "text-size": {"base": 1.2, "stops": [[10, 12], [15, 22]]}},
    paint={"text-color": "#333", "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1.2},
)

L(
    id="place_town",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    filter=["all", ["==", "class", "town"]],
    layout={
        "icon-image": {"base": 1, "stops": [[0, "dot_9"], [8, ""]]},
        "text-anchor": "bottom",
        "text-field": "{name_en}",
        "text-font": ["Roboto Regular"],
        "text-max-width": 8,
        "text-offset": [0, 0],
        "text-size": {"base": 1.2, "stops": [[7, 12], [11, 16]]},
    },
    paint={"text-color": "#333", "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1.2},
)

L(
    id="place_city",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    minzoom=5,
    filter=["all", ["==", "class", "city"]],
    layout={
        "icon-image": {"base": 1, "stops": [[0, "dot_9"], [8, ""]]},
        "text-anchor": "bottom",
        "text-field": "{name_en}",
        "text-font": ["Roboto Medium"],
        "text-max-width": 8,
        "text-offset": [0, 0],
        "text-size": {"base": 1.2, "stops": [[7, 14], [11, 24]]},
        "icon-allow-overlap": True,
        "icon-optional": False,
    },
    paint={"text-color": "#333", "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1.2},
)

L(
    id="state",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    maxzoom=6,
    filter=["all", ["==", "class", "state"]],
    layout={"text-field": "{name_en}", "text-font": ["Roboto Condensed Italic"], "text-size": {"stops": [[4, 11], [6, 15]]}, "text-transform": "uppercase"},
    paint={"text-color": "#633", "text-halo-color": "rgba(255,255,255,0.7)", "text-halo-width": 1},
)

L(
    id="country_3",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    filter=["all", [">=", "rank", 3], ["==", "class", "country"]],
    layout={"text-field": "{name_en}", "text-font": ["Roboto Condensed Italic"], "text-max-width": 6.25, "text-size": {"stops": [[3, 11], [7, 17]]}, "text-transform": "none"},
    paint={"text-color": "#334", "text-halo-blur": 1, "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1},
)

L(
    id="country_2",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    filter=["all", ["==", "rank", 2], ["==", "class", "country"]],
    layout={"text-field": "{name_en}", "text-font": ["Roboto Condensed Italic"], "text-max-width": 6.25, "text-size": {"stops": [[2, 11], [5, 17]]}, "text-transform": "none"},
    paint={"text-color": "#334", "text-halo-blur": 1, "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1},
)

L(
    id="country_1",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    filter=["all", ["==", "rank", 1], ["==", "class", "country"]],
    layout={"text-field": "{name_en}", "text-font": ["Roboto Condensed Italic"], "text-max-width": 6.25, "text-size": {"stops": [[1, 11], [4, 17]]}, "text-transform": "none"},
    paint={"text-color": "#334", "text-halo-blur": 1, "text-halo-color": "rgba(255,255,255,0.8)", "text-halo-width": 1},
)

L(
    id="continent",
    type="symbol",
    source="openmaptiles",
    sourceLayer="place",
    maxzoom=1,
    filter=["all", ["==", "class", "continent"]],
    layout={"text-field": "{name_en}", "text-font": ["Roboto Condensed Italic"], "text-size": 13, "text-transform": "uppercase", "text-justify": "center"},
    paint={"text-color": "#633", "text-halo-color": "rgba(255,255,255,0.7)", "text-halo-width": 1},
)
