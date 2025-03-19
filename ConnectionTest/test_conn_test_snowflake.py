import pytest

@pytest.mark.usefixture('snowflake_conn')
def test_snowflake_connection(snowflake_conn):
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT CURRENT_USER();")  # Simple test query
    result = cursor.fetchone()

    assert result is not None  # Ensure we got a result
    print(f"✅ Connected as: {result[0]}")  # Print the connected user

    cursor.close()
