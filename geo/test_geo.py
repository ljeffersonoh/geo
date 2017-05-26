import pytest
from shapely.geometry import shape, Point

# from geo.point_in_geojson import point_to_iraq
from geo import point_to_iraq


# @pytest.fixture
def test_nineveh():
    p = Point((42.451171875, 35.82672127366604))
    properties = point_to_iraq(p)
    assert properties['name:en'] == 'Nineveh'


# @pytest.fixture
def test_al_anbar():
    # "Al Anbar"
    p = Point((41.484375, 32.32427558887655))
    properties = point_to_iraq(p)
    assert properties['name:en'] == 'Al Anbar'


# @pytest.fixture
def test_diyala():
    # Diyala
    p = Point((45.120849609375, 33.86129311351553))
    properties = point_to_iraq(p)
    assert properties['name:en'] == 'Diyala'


