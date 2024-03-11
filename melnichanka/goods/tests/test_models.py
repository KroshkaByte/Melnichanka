import pytest
from goods.models import Brand, Factory, Flour, Goods, Package


@pytest.mark.django_db
@pytest.mark.parametrize(
    "crop, expected",
    [
        ("wheat", "wheat"),
        ("barley", "barley"),
        ("rye", "rye"),
    ],
)
def test__flour__create_flour_valid_name(crop, expected):
    flour_test = Flour.objects.create(flour_name=crop)
    assert flour_test.flour_name == expected


@pytest.mark.django_db
@pytest.mark.parametrize(
    "brand, expected",
    [
        ("dolce_gabbana", "dolce_gabbana"),
        ("Gucci", "Gucci"),
        ("Nike", "Nike"),
    ],
)
def test__brand__create_brand_valid_name(brand, expected):
    brand_test = Brand.objects.create(brand=brand)
    assert brand_test.brand == expected


# @pytest.mark.django_db
# @pytest.mark.parametrize(
#     "package, expected", [
#         (50, 50),
#         (100, 100),
#         (200, 200),
#     ])
# def test__package__create_package_valid_package(package, expected):
#     package_test = Package.objects.create(package=package)
#     assert package_test.package == expected
