import json
import geojson
from shapely.geometry import shape, Point

import logging
logging.basicConfig(level=0, format='')
log = logging.getLogger('test')


"""
given a GeoJSON object, we want to be able to determine if the Point is in the region


# Basic geoinferencing with Shapely, GeoJSON and OpenRefine
# http://www.mhermans.net/geojson-shapely-geocoding.html

# https://macwright.org/2015/03/23/geojson-second-bite.html


given a point, determine the "name:en" that the point is in

        "name:en": "Najaf",

"""



def point_to_iraq(point):
    """
    returns a json of the properties of teh 
    """

    with open('data/admin_level_4.geojson', 'r') as f:
        admin_level_4 = json.load(f)

    # for feature in admin_level_4['features']:
    #     if feature.get('properties'):
    #         if feature.get('properties').get('name:en'):
    #             print feature['properties']['name:en']

    for feature in admin_level_4['features']:
        # print feature['properties']

        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            properties = feature['properties']
            name = properties.get('name')
            name_display = properties.get('name:en')

            # log.info('Name      : %s' % name)
            # log.info('Name (en) : %s' % name_display)
        
            return properties

    return None
        