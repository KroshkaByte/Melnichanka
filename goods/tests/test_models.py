import pytest


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
