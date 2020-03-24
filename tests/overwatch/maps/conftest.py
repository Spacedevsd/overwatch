import pytest
from tests.util import load_mockup


@pytest.fixture
def maps_html():
    return load_mockup("maps.html")
