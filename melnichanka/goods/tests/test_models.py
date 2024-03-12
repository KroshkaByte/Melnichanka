import pytest
from goods.models import Brand, Factory, Flour, Goods


@pytest.mark.django_db
def test__flour__create_object_valid(flour_object):
    assert flour_object.flour_name == "name_flour"


@pytest.mark.django_db
def test__flour__get_object_valid(flour_object):
    retrieved_flour = Flour.objects.get(id=flour_object.id)
    assert retrieved_flour.flour_name == "name_flour"


@pytest.mark.django_db
def test__brand__create_brand_valid(brand_object):
    assert brand_object.brand == "name_brand"


@pytest.mark.django_db
def test__brand__get_object_valid(brand_object):
    retrieved_brand = Brand.objects.get(id=brand_object.id)
    assert retrieved_brand.brand == "name_brand"


@pytest.mark.django_db
def test__factory__create_object_valid(factory_object):
    assert factory_object.full_name == "Курский Комбинат Хлебопродуктов"
    assert factory_object.short_name == "ККХП"
    assert factory_object.full_address == "305025, г. Курск, проезд Магистральный, 22Г"
    assert factory_object.departure_city == "Курск"
    assert factory_object.departure_station_branch == "Московская ж/д"
    assert factory_object.departure_station_id == 208108
    assert factory_object.departure_station_name == "Рышково"


@pytest.mark.django_db
def test__factory__get_object_valid(factory_object):
    retrieved_factory = Factory.objects.get(id=factory_object.id)
    assert retrieved_factory.full_name == factory_object.full_name
    assert retrieved_factory.short_name == factory_object.short_name
    assert retrieved_factory.full_address == factory_object.full_address
    assert retrieved_factory.departure_city == factory_object.departure_city
    assert (
        retrieved_factory.departure_station_branch
        == factory_object.departure_station_branch
    )
    assert retrieved_factory.departure_station_id == factory_object.departure_station_id
    assert (
        retrieved_factory.departure_station_name
        == factory_object.departure_station_name
    )


@pytest.mark.django_db
def test__package__create_object_valid_package(package_object):
    assert package_object.package == 1


@pytest.mark.django_db
def test__package__create_object_valid_pallet_weight(package_object):
    assert package_object.pallet_weight == 1000


@pytest.mark.django_db
def test__goods__create_object_valid(
    goods_object, flour_object, brand_object, package_object
):
    assert goods_object.flour_name == flour_object
    assert goods_object.brand == brand_object
    assert goods_object.package == package_object
    assert goods_object.price == 10000


@pytest.mark.django_db
def test__goods__get_object_valid(goods_object):
    retrieved_goods = Goods.objects.get(id=goods_object.id)
    assert retrieved_goods.flour_name == goods_object.flour_name
    assert retrieved_goods.brand == goods_object.brand
    assert retrieved_goods.package == goods_object.package
    assert retrieved_goods.price == goods_object.price


@pytest.mark.django_db
def test__goods__return_valid_str(goods_object):
    assert (
        str(goods_object)
        == "name_flour, т/м name_brand, 1 кг, Курский Комбинат Хлебопродуктов кг"
    )


@pytest.mark.django_db
def test__flour__return_valid_str(flour_object):
    assert str(flour_object) == "name_flour"


@pytest.mark.django_db
def test__brand__return_valid_str(brand_object):
    assert str(brand_object) == "name_brand"


@pytest.mark.django_db
def test__package__return_valid_str(package_object):
    assert str(package_object) == "1 кг, Курский Комбинат Хлебопродуктов"


@pytest.mark.django_db
def test__factory__return_valid_str(factory_object):
    assert str(factory_object) == "Курский Комбинат Хлебопродуктов"
