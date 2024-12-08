import sqlite3
from sqlite3 import Error
# Connect to SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
# Function to add a new allergen
def add_allergen(conn, allergen):
    sql = ''' INSERT INTO allergens(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (allergen,))
    conn.commit()
    return cur.lastrowid
# Function to display all flavors
def display_flavors(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM flavors")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Function to search flavors by name
def search_flavors(conn, search_term):
    cur = conn.cursor()
    cur.execute("SELECT * FROM flavors WHERE name LIKE ?", ('%' + search_term + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Function to add an item to cart
def add_to_cart(conn, product_name):
    sql = ''' INSERT INTO cart(product_name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (product_name,))
    conn.commit()
    return cur.lastrowid
# Function to display the cart
def display_cart(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM cart")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Function to display allergens
def display_allergens(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM allergens")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Function to display customer suggestions
def display_suggestions(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer_suggestions")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Main function
def main():
    database = r"ice_cream_parlor.db"
    conn = create_connection(database)
    if conn is not None:
        with conn:
            # Example usage:
            # Add a new allergen
            allergen_name = 'Gluten'
            add_allergen(conn, allergen_name)
            # Display all flavors
            print("All flavors:")
            display_flavors(conn)
            # Search for flavors
            search_term = 'Vanilla'
            print(f"Search results for '{search_term}':")
            search_flavors(conn, search_term)
            # Add an item to the cart
            product_name = 'Vanilla'  # Assuming 'Vanilla' is a flavor name
            add_to_cart(conn, product_name)
            # Display the cart
            print("Current cart:")
            display_cart(conn)
            # Display allergens
            print("Allergens:")
            display_allergens(conn)
            # Display customer suggestions
            print("Customer suggestions:")
            display_suggestions(conn)
    else:
        print("Error! Cannot create the database connection.")
if __name__ == '__main__':
    main()
