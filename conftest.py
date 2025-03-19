import pytest
import snowflake.connector
from cryptography.hazmat.primitives import serialization
import os

@pytest.fixture(scope="module")

def snowflake_conn():
    account = os.getenv("SNOWFLAKE_ACCOUNT")  # HidingSensitive Data
    user = os.getenv("SNOWFLAKE_USER")
    private_key_path = os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH")
    if not all([account, user, private_key_path]):
        raise ValueError("Missing environment variables for Snowflake connection!")

    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # No password since we removed it
    )
# Connect to Snowflake
    conn = snowflake.connector.connect(
        account=account, #HidingSensitive Data
        user=user,
        private_key=private_key,
        role="ACCOUNTADMIN"
    )
    yield conn
    conn.close()
