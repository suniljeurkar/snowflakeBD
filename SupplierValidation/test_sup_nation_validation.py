def test_null_orders(snowflake_conn):
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT S_SUPPKEY,S_NAME FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER "
                   "WHERE S_NATIONKEY NOT IN ( SELECT N_NATIONKEY FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION);")
    result = cursor.fetchall()
    cursor.close()
    assert not result , f"Data Integrity Issue: Some Supplier are not connected to nation"
    print("All Supplier Connected to Nations")

#pytest -v --html=reports\report.html --self-contained-html