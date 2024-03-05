from models import Brand


def test__access_to_brand_model():
    assert hasattr(Brand, "objects")
