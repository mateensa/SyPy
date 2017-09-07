import psycopg2


try:
    #conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='1234'");
    conn = psycopg2.connect("dbname='dwa' user='integration_user' "
                            "host='xxxxxx.cmj8jk61oxi0.us-west-2.redshift.amazonaws.com' password='xxxxxxxxxx' port='5439'");
    print("I am able to connect to the database");
    cursor = conn.cursor()
    cursor.execute("select count(1) from presentation.sales_order_f ")
    records = cursor.fetchall()
    print(records)
except:
    print("---->I am unable to connect to the database");
