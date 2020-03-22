import pytest

from .util import load_mockup


@pytest.fixture
def heroes_html():
    return load_mockup("heroes.html")


@pytest.fixture
def hero_html():
    return load_mockup("hero.html")


@pytest.fixture
def hero2_html():
    return load_mockup("hero2.html")


@pytest.fixture
def hero3_html():
    return load_mockup("hero3.html")


@pytest.fixture
def ashe_html():
    return load_mockup("ashe.html")
