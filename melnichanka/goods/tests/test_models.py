import pytest
from django.core.exceptions import ValidationError

from ..models import Brand, Factory, Flour, Goods, Package


@pytest.fixture
def flour():
    return Flour.objects.create(flour_name="Test Flour")


@pytest.fixture
def brand():
    return Brand.objects.create(brand="Test Brand")


@pytest.fixture
def package():
    factory = Factory.objects.create(
        full_name="Test Factory",
        short_name="Test Factory Short",
        full_address="Test Address",
        departure_city="Test City",
        departure_station_branch="Test Branch",
        departure_station_id=123,
        departure_station_name="Test Station",
    )
    return Package.objects.create(package=50, factory=factory, pallet_weight=1000)


@pytest.mark.parametrize(
    "flour, brand, package, price",
    [
        (flour, brand, package, 100.00),
        (flour, brand, package, 200.00),
        (flour, brand, package, 300.00),
    ],
)
def test_goods_creation(flour, brand, package, price):
    goods = Goods.objects.create(
        flour_name=flour,
        brand=brand,
        package=package,
        price=price,
    )
    assert goods.flour_name == flour
    assert goods.brand == brand
    assert goods.package == package
    assert goods.price == price
    assert str(goods) == f"{flour}, т/м {brand}, {package.package} кг"


@pytest.mark.parametrize(
    "flour, brand, package, price",
    [
        (flour, brand, package, -10.00),
        (flour, brand, package, 0.00),
        (flour, brand, package, 10000.00),
    ],
)
def test_goods_price_validation(flour, brand, package, price):
    with pytest.raises(ValidationError):
        Goods.objects.create(
            flour_name=flour,
            brand=brand,
            package=package,
            price=price,
        )


def test_goods_unique_together(flour, brand, package):
    Goods.objects.create(
        flour_name=flour,
        brand=brand,
        package=package,
        price=100.00,
    )
    with pytest.raises(ValidationError):
        Goods.objects.create(
            flour_name=flour,
            brand=brand,
            package=package,
            price=200.00,
        )
