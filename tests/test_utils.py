import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["f.keil@ga.com", "b@c.com", "34908432%@5678.com.er"]
)
def test_positive_check_valid_email(address):
    """Ensure e-mail is valid"""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["f.keil@g%a.com", "b@ccom", "34908432%@5678.com.er-"]
)
def test_negative_check_valid_email(address):
    """Ensure e-mail is invalid"""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test Generation of random simple password
    TODO: Generate hashed complex passwords, encrypt it
    """
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))

    assert len(set(passwords)) == 100
