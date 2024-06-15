import pytest


@pytest.mark.django_db
def test__goods__return_valid_str(goods_object, flour_object, brand_object, package_object):
    assert (
        str(goods_object)
        == f"{flour_object.flour_name}, т/м {brand_object.brand}, {package_object} кг"
    )


@pytest.mark.django_db
def test__flour__return_valid_str(flour_object):
    assert str(flour_object) == flour_object.flour_name


@pytest.mark.django_db
def test__brand__return_valid_str(brand_object):
    assert str(brand_object) == brand_object.brand


@pytest.mark.django_db
def test__package__return_valid_str(package_object, factory_object):
    assert str(package_object) == f"{package_object.package}"


@pytest.mark.django_db
def test__factory__return_valid_str(factory_object):
    assert str(factory_object) == factory_object.full_name
