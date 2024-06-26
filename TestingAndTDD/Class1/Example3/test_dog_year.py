import pytest

import dog_year


@pytest.mark.parametrize("human_years, dog_age", [(15, 73.0), (1, 10.5), (9, 49.0), (7, 41.0)])
def test_get_dog_years(human_years, dog_age):
    """" Evaluating that human years converts do dog years correctly"""
    # (15 ,73.0), (1, 10.5), (9,49.0), (7,41.0)
    assert dog_year.get_dog_years(human_years) == dog_age

