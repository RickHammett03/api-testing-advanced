"""
Fixtures globales para pytest
"""

import pytest
from utils.auth import get_token


@pytest.fixture
def auth_token():
    """
    Fixture que genera token automáticamente
    """
    return get_token()