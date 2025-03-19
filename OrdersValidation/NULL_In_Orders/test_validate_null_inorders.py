def test_null_orders(snowflake_conn):
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS WHERE O_CUSTKEY IS NULL OR O_ORDERDATE IS NULL;")
    result = cursor.fetchall()
    cursor.close()
    assert not result , f"Data Integrity Issue: Some Orders Or Customer Key has null values!"
    print("All Order and Customer Id keys are not null")
