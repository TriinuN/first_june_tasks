import pytest

import century


@pytest.mark.parametrize("year, result", [(2014, 'You are in the 21 century'),
                                          (-1, "Nice! You are not even in a first century yet!")])
def test_get_century(year, result):
    """" Testing if it says what century it is """
    assert century.get_century(year) == result
