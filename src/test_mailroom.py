"""This is our tests for our mailroom madness program."""

DONORS = {
    'ANNA SHELBY': [300],
    'MORGAN NOMURA': [10],
    'EDGAR POE': [1000]
}


def test_validate_user_name_input():
    """Test for checking the user input is a first and last name."""


def test_show_list():
    """Test for showing donors list is a list."""
    from mailroom import show_list
    assert show_list(DONORS) == ['ANNA SHELBY', 'EDGAR POE', 'MORGAN NOMURA']


def test_find_donor():
    """Test to determine a new user has been added."""
    from mailroom import find_donor
    assert find_donor('CAT POWERS', DONORS) == []
