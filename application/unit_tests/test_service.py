import pytest
from application.service.validation import *
from application.service.data_handling import *


def test_amount_validation():
    assert validate_amount(1) == 1
    assert validate_amount(0) == 0
    assert validate_amount('qwe') == 0
    assert validate_amount(1.000001) == 0


def test_currency_validation():
    assert validate_currency('643') == 1
    assert validate_currency('840') == 1
    assert validate_currency('978') == 1
    assert validate_currency('122') == 0


def test_data_hashing():
    assert data_to_hash({'q': '1', 'w': 2}, ('q'), 'secret') == \
                {'q': '1', 'w': 2, 'sign': 'a4b9775cad7a19b8563ecf41994868f50ef75403a5942788b15410305be762be'}
    assert data_to_hash({}, (), 'secret') == \
                {'sign': '2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b'}
    with pytest.raises(TypeError):
        data_to_hash({}, 1, '')
