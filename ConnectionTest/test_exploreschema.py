import pytest
import snowflake.connector
actual_schema = ['CUSTOMER', 'LINEITEM', 'REGION', 'SUPPLIER', 'ORDERS', 'PARTSUPP', 'NATION', 'PART']

#Set Before Proceeding
db = 'SNOWFLAKE_SAMPLE_DATA'
sys_schema = 'INFORMATION_SCHEMA'
table_schema = 'TPCH_SF1'

@pytest.mark.usefixtures('snowflake_conn')
def test_explore_schema(snowflake_conn:snowflake.connector):
    cursor = snowflake_conn.cursor()
    cursor.execute(f"SELECT TABLE_NAME FROM {db}.{sys_schema}.TABLES WHERE TABLE_SCHEMA ='{table_schema}';")  # Simple test query
    tables = [row[0] for row in cursor.fetchall()]
    print(f"Tables in TPCH_SF1 Schema {tables}")
    cursor.close()
    missing_tables = []
    for tbn in actual_schema:
        if tbn not in tables:
            print(f"Missing table: {tbn}")
            missing_tables.append(tbn)
        else:
            print(f"Found table {tbn}")
    assert len(tables)>0, "No Tables found in Schema!"
    assert not missing_tables, f"Missing Tables : {missing_tables}"
    print(f"✅ No missing tables found!, total tables {len(tables)} found")
