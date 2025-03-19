import csv
import os
from pandas.io.common import file_exists


def test_orders_without_customers(snowflake_conn):
    cursor = snowflake_conn.cursor()
    querry = """SELECT O_ORDERKEY FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS 
                WHERE O_CUSTKEY NOT IN (SELECT C_CUSTKEY FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER);
            """
    cursor.execute(querry)
    result = cursor.fetchall()
    cursor.close()
    file_path = "BusinessValidation/failed_exports/orderWOcustomers.csv"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if result: #if result is true

        with open (file_path,mode="a" if file_exists else "w",newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["O_ORDERKEY"])  # SETTINGUP HEADER

            writer.writerows(result)
        print(f"{len(result)} orders invalid customers are saved to {file_path}")
    assert not result , f"Orders with invalid customers found! Check {file_path}"
    print("Orders vs Customers matched correctly")

#pytest -v --html=reports\report.html --self-contained-html