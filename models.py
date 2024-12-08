from database import create_connection
class Flavor:
    def __init__(self, name, season):
        self.name = name
        self.season = season
    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flavors (name, season) VALUES (?, ?)', (self.name, self.season))
        conn.commit()
        conn.close()
    @staticmethod
    def all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM flavors')
        rows = cursor.fetchall()
        conn.close()
        return rows
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (self.name, self.quantity))
        conn.commit()
        conn.close()
    @staticmethod
    def all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ingredients')
        rows = cursor.fetchall()
        conn.close()
        return rows
class Allergen:
    def __init__(self, name):
        self.name = name
    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO allergens (name) VALUES (?)', (self.name,))
        conn.commit()
        conn.close()
    @staticmethod
    def all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM allergens')
        rows = cursor.fetchall()
        conn.close()
        return rows
class CustomerSuggestion:
    def __init__(self, flavor_name, allergen_concern):
        self.flavor_name = flavor_name
        self.allergen_concern = allergen_concern
    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer_suggestions (flavor_name, allergen_concern) VALUES (?, ?)', (self.flavor_name, self.allergen_concern))
        conn.commit()
        conn.close()
    @staticmethod
    def all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customer_suggestions')
        rows = cursor.fetchall()
        conn.close()
        return rows
class Cart:
    def __init__(self, product_name):
        self.product_name = product_name
    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cart (product_name) VALUES (?)', (self.product_name,))
        conn.commit()
        conn.close()
    @staticmethod
    def all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cart')
        rows = cursor.fetchall()
        conn.close()
        return rows
