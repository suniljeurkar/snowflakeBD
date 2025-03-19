def test_data_int(snowflake_conn):
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT O_ORDERKEY,O_CUSTKEY, O_ORDERDATE FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS "
                   "WHERE O_CUSTKEY NOT IN (SELECT C_CUSTKEY FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER);")
    result = cursor.fetchall()
    cursor.close()
    assert not result , f"Data Integrity Issue: Some Orders have invalid customers!"
    print("All orders have valid customers!")
