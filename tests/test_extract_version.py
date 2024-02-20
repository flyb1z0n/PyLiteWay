import pytest
from pyliteway.migrator import extract_version

def test_valid_version():
    assert extract_version("V0001__test_example.sql") == "0001"

def test_invalid():
    with pytest.raises(ValueError):
        assert extract_version("Vtest_example.sql")