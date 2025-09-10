
from src.core import patterns


def test_patterns_keys():
    assert "apache_common" in patterns.PATTERNS
    assert "auth" in patterns.PATTERNS

