import pytest
from django.db import IntegrityError

from goods.models import Flour


# @pytest.mark.django_db
def test_flour_creation(db):
    with pytest.raises(IntegrityError):
        Flour.objects.create(flour_name="wheat")
        Flour.objects.create(flour_name="wheat")


# @pytest.mark.django_db
# def test_flour_str():
#     flour = Flour.objects.create(flour_name="wheat")
#     assert str(flour) == "wheat"


# @pytest.mark.django_db
# def test_brand_creation():
#     with pytest.raises(IntegrityError):
#         Brand.objects.create(brand="test_brand")
#         Brand.objects.create(brand="test_brand")


# @pytest.mark.django_db
# def test_brand_str():
#     brand = Brand.objects.create(brand="test_brand")
#     assert str(brand) == "test_brand"


# @pytest.mark.django_db
# def test_package_creation():
#     with pytest.raises(IntegrityError):
#         Package.objects.create(
#             package=50, factory=Factory.objects.create(full_name="test_factory")
#         )
#         Package.objects.create(
#             package=50, factory=Factory.objects.create(full_name="test_factory")
#         )


# @pytest.mark.django_db
# def test_package_str():
#     package = Package.objects.create(
#         package=50, factory=Factory.objects.create(full_name="test_factory")
#     )
#     assert str(package) == "50 кг, test_factory"


# @pytest.mark.django_db
# def test_factory_creation():
#     with pytest.raises(IntegrityError):
#         Factory.objects.create(full_name="test_factory")
#         Factory.objects.create(full_name="test_factory")


# @pytest.mark.django_db
# def test_factory_str():
#     factory = Factory.objects.create(full_name="test_factory")
#     assert str(factory) == "test_factory"


# @pytest.mark.django_db
# def test_goods_creation():
#     Goods.objects.create(
#         flour_name=Flour.objects.create(flour_name="wheat"),
#         brand=Brand.objects.create(brand="test_brand"),
#         package=Package.objects.create(
#             package=50, factory=Factory.objects.create(full_name="test_factory")
#         ),
#         price=100,
#     )
#     assert Goods.objects.count() == 1


# @pytest.mark.django_db
# def test_goods_unique_together():
#     Goods.objects.create(
#         flour_name=Flour.objects.create(flour_name="wheat"),
#         brand=Brand.objects.create(brand="test_brand"),
#         package=Package.objects.create(
#             package=50, factory=Factory.objects.create(full_name="test_factory")
#         ),
#         price=100,
#     )
#     with pytest.raises(IntegrityError):
#         Goods.objects.create(
#             flour_name=Flour.objects.create(flour_name="wheat"),
#             brand=Brand.objects.create(brand="test_brand"),
#             package=Package.objects.create(
#                 package=50, factory=Factory.objects.create(full_name="test_factory")
#             ),
#             price=101,
#         )
