import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def main():
    database = r"ice_cream_parlor.db"
    sql_create_allergens_table = """ CREATE TABLE IF NOT EXISTS allergens (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL
                                    ); """
    sql_create_customer_suggestions_table = """ CREATE TABLE IF NOT EXISTS customer_suggestions (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                flavor_name TEXT NOT NULL,
                                                allergen_concern TEXT
                                            ); """
    sql_create_ingredients_table = """ CREATE TABLE IF NOT EXISTS ingredients (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        quantity INTEGER
                                    ); """
    sql_create_cart_table = """ CREATE TABLE IF NOT EXISTS cart (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                product_name TEXT NOT NULL
                            ); """
    sql_create_flavors_table = """ CREATE TABLE IF NOT EXISTS flavors (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    season TEXT
                                ); """
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_allergens_table)
        create_table(conn, sql_create_customer_suggestions_table)
        create_table(conn, sql_create_ingredients_table)
        create_table(conn, sql_create_cart_table)
        create_table(conn, sql_create_flavors_table)
    else:
        print("Error! Cannot create the database connection.")
if __name__ == '__main__':
    main()
