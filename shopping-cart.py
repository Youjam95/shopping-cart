# shopping_cart.py

#Date & time librarry importing 
import datetime as dt
# The list of products in the inventory
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#Defining variables & contants 
product_ids= list ( range( 1, len(products ) +1 ) ) 
strproduct_ids= [ str(item) for item in product_ids ] # str list with all the ids
sub_total= 0 
selected_ids= [ ]
selected_id = 0
TAX_RATE = 0.0875 # Washington, NYC sales tax rate (constant)
# User defined functions ( To add a $ sign to the price )

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#  Capturing valid inputs / End of process / Handling all invalid inputs 

checkout_start_at = dt.datetime.now() 
while True : 
     selected_id = input("Please input the product ID")

     if selected_id == "DONE" : break 
     elif selected_id not in strproduct_ids : print (" Invalid id, try again") 
     else  : selected_ids.append(selected_id)

### output 
print("---------------------------------")
print(" Daily-Fresh Grocery")
print("WWW.Fresh-Grocery.com")
print("---------------------------------")
print("CHECKOUT AT: " + checkout_start_at.strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------------")
print("SELECTED PRODUCTS:")
print("---------------------------------")

for selected_id in selected_ids:
      matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
      matching_product = matching_products[0]
      sub_total = sub_total + matching_product["price"]
      print(" .... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

print(" ....Sub_total  = " + str(to_usd(sub_total)) )
print(" ....Sales tax  = " + str(to_usd(sub_total*TAX_RATE)))
print(" ....Total      = " + str(to_usd(sub_total*(1+TAX_RATE))))
print("---------------------------------")
print(" Thank you forshopping with us, see you again")
print("---------------------------------")
