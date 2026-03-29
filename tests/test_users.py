from utils.api_client import get
from data.test_data import USER_IDS
from jsonschema import validate
from schemas.user_schema import user_schema
import pytest


@pytest.mark.parametrize("user_id", USER_IDS)
def test_get_single_user(auth_token, user_id):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = get(f"/users/{user_id}", headers=headers)

    assert response.status_code == 200

    data = response.json()

    # Validación de schema
    validate(instance=data, schema=user_schema)

    # Validación adicional
    assert data["id"] == user_id