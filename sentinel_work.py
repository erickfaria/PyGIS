# Importações dos pacotes

import arcgis
from arcgis import geometry
from arcgis.geometry import Geometry
from arcgis.gis import GIS
from arcgis.geocoding import geocode
from arcgis.raster.functions import stretch, extract_band, apply, composite_band, colormap, remap, ndvi, NDVI
import pandas as pd
import datetime as dt
import sys
import math
import numpy as np
from bokeh.models import Range1d
from bokeh.plotting import figure, show, output_notebook
from IPython.display import clear_output, HTML
from ipywidgets import *
import matplotlib.pyplot as plt


def exact_search(my_gis, title, owner_value, item_type_value):
    final_match = None
    search_result = my_gis.content.search(query=title + ' AND owner' + owner_value, item_type=item_type_value,
                                          outside_org=True)

    if 'Imagery Layer' in item_type_value:
        item_type_value = item_type_value.replace('Imagery Layer', 'Image Service')
    elif 'Layer' in item_type_value:
        item_type_value = item_type_value.replace('Layer', 'Service')

    for result in search_result:
        if result.title == title and result.type == item_type_value:
            final_match = result
            break
    return final_match


satellite_item = exact_search(gis, 'Sentinel-2 Views', 'esri', 'Imagery Layer')
satellite = satellite_item.layers[0]


def filter_images(my_map, start_datetime, end_datetime, extend=area['extend']):
    geom_obj = Geometry(extend)
    selected = satellite.filter_by(where='(Category = 1) AND (CloudCover <=0.025)',
                                   time=[start_datetimr, end_datetime],
                                   geometry=geometry.filters.intersects(geom_obj))

    id_list = slected.filtered_rasters()
    print('Applicable lockRasterIds=', id_list)

    if not id_list:
        return None
    else:
        date_title_from = start_datetime.strftime('%m%d%y')
        date_title_to = end_datetime.strftime('%m%d%y')

        my_map.add_layer(selected.mean(), {'title': date_title_from + 'to' + date_title_to + 'at' + address})

        fs = selected.query(out_fields='AcquisitionDate, name, CloudCover')
        tdf = fs.sdf

        return [tdf, selected]


def call_filter_images(my_map, date_str, extent=area['extent']):
    datetime_object = dt.datetime.strptime(date_str, '%Y-%m-%d')
    start_datetime = datetime_object - dt.timedelta(days=num_dias)
    end_datetime = datetime_object + dt.timedelta(days=num_dias + 1)
    [tdf, selected] = filter_images(my_map, start_datetime, end_datetime, extent=area['extent'])

    if tdf is not None:
        display(tdf.head())
    return selected

num_dias = 16
address = ''
location = {'x': ,
            'y':
            'spatialReference': {''}}

area = geocode(address, out_sr=satellite.properties.spatialReference)[0]




