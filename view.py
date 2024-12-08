from models import Flavor, Ingredient, Allergen, CustomerSuggestion, Cart
def add_flavor(name, season):
    flavor = Flavor(name, season)
    flavor.save()
def add_ingredient(name, quantity):
    ingredient = Ingredient(name, quantity)
    ingredient.save()
def add_allergen(name):
    allergen = Allergen(name)
    allergen.save()
def add_customer_suggestion(flavor_name, allergen_concern):
    suggestion = CustomerSuggestion(flavor_name, allergen_concern)
    suggestion.save()
def add_to_cart(product_name):
    cart_item = Cart(product_name)
    cart_item.save()
def view_flavors():
    return Flavor.all()
def view_ingredients():
    return Ingredient.all()
def view_allergens():
    return Allergen.all()
def view_customer_suggestions():
    return CustomerSuggestion.all()
def view_cart():
    return Cart.all()
def search_flavors_by_season(season):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM flavors WHERE season = ?', (season,))
    rows = cursor.fetchall()
    conn.close()
    return rows
