"""This is our tests for our mailroom madness program."""


DONORS = {
    'ANNA SHELBY': [300],
    'MORGAN NOMURA': [10],
    'EDGAR POE': [1000]
}


def test_show_list():
    """Test for showing donors list is a list."""
    from mailroom import show_list
    assert show_list(DONORS) == ['ANNA SHELBY', 'EDGAR POE', 'MORGAN NOMURA']


def test_find_donor():
    """Test to determine a new user has been added."""
    from mailroom import find_donor
    assert find_donor('CAT POWERS', DONORS) == []


def test_build_email():
    """Test to determine if the correct donor and donation."""
    from mailroom import build_email
    assert 'EDGAR POE', 1000 in build_email('EDGAR POE')
