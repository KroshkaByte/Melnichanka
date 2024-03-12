import pytest
from goods.models import Brand, Factory, Flour, Goods, Package


@pytest.fixture
def factory_object():
    return Factory.objects.create(
        full_name="Курский Комбинат Хлебопродуктов",
        short_name="ККХП",
        full_address="305025, г. Курск, проезд Магистральный, 22Г",
        departure_city="Курск",
        departure_station_branch="Московская ж/д",
        departure_station_id=208108,
        departure_station_name="Рышково",
    )


@pytest.fixture
def flour_object():
    return Flour.objects.create(flour_name="name_flour")


@pytest.fixture
def brand_object():
    return Brand.objects.create(brand="name_brand")


@pytest.fixture
def package_object(factory_object):
    return Package.objects.create(package=1, factory=factory_object, pallet_weight=1000)


@pytest.fixture
def goods_object(flour_object, brand_object, package_object):
    return Goods.objects.create(
        flour_name=flour_object,
        brand=brand_object,
        package=package_object,
        price=10000,
    )
