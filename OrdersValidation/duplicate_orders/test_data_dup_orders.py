def test_dupes(snowflake_conn):
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT O_ORDERKEY, COUNT(*) FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS GROUP BY O_ORDERKEY HAVING COUNT(*)>1;")
    result = cursor.fetchall()
    cursor.close()
    assert not result , f"Data Integrity Issue: Some Orders have Duplicate Values!"
    print("All Order Keys are unique")
