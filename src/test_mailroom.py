"""This is our tests for our mailroom madness program."""
import pytest

DONORS = {
    'ANNA SHELBY': [300, 10, 15],
    'MORGAN NOMURA': [10, 200, 50],
    'EDGAR POE': [1000]
}


DONORS_2 = {
    'ANNA SHELBY': [300, 10, 15],
    'MORGAN NOMURA': [10, 200, 50],
    'EDGAR POE': [1000]
}


REPORT_ENTRY = 'EDGAR POE                     1000.00             1                   1000.00'


def test_validate_user_prompt():
    """Test to determine if letter command input is valid."""
    from mailroom import validate_user_prompt, user_prompt
    assert validate_user_prompt('T', ['T', 'R', 'Q'], user_prompt) == 'T'


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


def test_build_report():
    """Test to determine if the correct donor and donation."""
    from mailroom import build_report
    assert REPORT_ENTRY in build_report(DONORS_2)
