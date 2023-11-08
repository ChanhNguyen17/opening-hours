from src.utils import convert_unix_to_string


def test_convert_unix_to_string_valid():
    # Test valid UNIX times
    assert convert_unix_to_string(3600) == "1 AM"
    assert convert_unix_to_string(3780) == "1:03 AM"
    assert convert_unix_to_string(7200) == "2 AM"
    assert convert_unix_to_string(64800) == "6 PM"
    assert convert_unix_to_string(86399) == "11:59:59 PM"


def test_convert_unix_to_string_invalid():
    # Test invalid UNIX times
    assert convert_unix_to_string(-1) == "Invalid UNIX time"
    assert convert_unix_to_string(86400) == "Invalid UNIX time"
    assert convert_unix_to_string(100000) == "Invalid UNIX time"


def test_convert_unix_to_string_edge_cases():
    # Test edge cases
    assert convert_unix_to_string(0) == "12 AM"  # Midnight
    assert convert_unix_to_string(43200) == "12 PM"  # Noon
