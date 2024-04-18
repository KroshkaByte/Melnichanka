import pytest

from goods.models import Brand, Factory, Flour, Package, Product


@pytest.fixture
def factory_object(faker):
    return Factory.objects.create(
        full_name=faker.pystr(),
        short_name=faker.pystr(),
        full_address=faker.address(),
        departure_city=faker.city(),
        departure_station_branch=faker.pystr(),
        departure_station_id=faker.pyint(min_value=1, max_value=999999),
        departure_station_name=faker.pystr(),
    )


@pytest.fixture
def flour_object(faker):
    return Flour.objects.create(flour_name=faker.pystr())


@pytest.fixture
def brand_object(faker):
    return Brand.objects.create(brand=faker.pystr())


@pytest.fixture
def package_object(factory_object, faker):
    return Package.objects.create(
        package=faker.pyint(), factory=factory_object, pallet_weight=faker.pyint()
    )


@pytest.fixture
def goods_object(flour_object, brand_object, package_object, faker):
    return Product.objects.create(
        flour_name=flour_object,
        brand=brand_object,
        package=package_object,
        price=faker.pyint(),
    )
