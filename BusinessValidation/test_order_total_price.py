import csv
import os
from pandas.io.common import file_exists


def test_total_orders_vs_lineitem_total(snowflake_conn):
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT O_ORDERKEY FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS "
                   "JOIN SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM ON O_ORDERKEY = L_ORDERKEY "
                   "GROUP BY O_ORDERKEY , O_TOTALPRICE HAVING O_TOTALPRICE <> SUM(L_EXTENDEDPRICE);")
    result = cursor.fetchall()
    cursor.close()
    file_path = "BusinessValidation/failed_exports/mismatched_orders.csv"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if result: #if result is true

        with open (file_path,mode="a" if file_exists else "w",newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["O_ORDERKEY"])  # SETTINGUP HEADER

            writer.writerows(result)
        print(f"{len(result)} orders with mismatched totals saved to {file_path}")
    assert not result , f"Order total does not match line items , see {file_path} for details"
    print("Order totals match correctly.")

#pytest -v --html=reports\report.html --self-contained-html