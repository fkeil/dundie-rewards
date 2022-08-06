import pytest

from dundie.core import load

from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(
    request,
):  # noqa se colocar create_new_file dentro dos parenteses, apenas esta funcao vai usar as novas pastas de teste
    """ "Test function load function"""
    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(
    request,
):  # noqa se colocar create_new_file dentro dos parenteses, apenas esta funcao vai usar as novas pastas de teste
    """ "Test function load function"""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Helpert"
