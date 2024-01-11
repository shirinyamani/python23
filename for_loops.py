#!/usr/bin/env python
# coding: utf-8

# In[ ]:
products = [
    {"name": "Laptop", "category": "Electronics", "price": 999.99},
    {"name": "Smartphone", "category": "Electronics", "price": 699.99},
    {"name": "Book: The Alchemist", "category": "Books", "price": 14.99},
    {"name": "Book: Harry Potter", "category": "Books", "price": 29.99},
    {"name": "Bluetooth Headphones", "category": "Electronics", "price": 199.99},
    {"name": "Monitor", "category": "Electronics", "price": 149.99},
    {"name": "Book: Python Programming", "category": "Books", "price": 49.99},
    {"name": "Desk Lamp", "category": "Furniture", "price": 24.99},
    {"name": "Mousepad", "category": "Accessories", "price": 5.99},
    {"name": "Stylus Pen", "category": "Accessories", "price": 12.99},
]


# 1. Generate a list of product names that are in the category "Electronics".
electronic_items = [product["name"] for product in products if product["category"] == "Electronics"]
print("electronic items:", electronic_items)



# %%
# 3. Compute the average price of all the products in the "Books" category.
books_prices = [product["price"] for product in products if product["category"] == "Books"]
avrg = sum(books_prices) / len(books_prices) if books_prices else 0
print(avrg)
# %%
# *args like siahchale get everything inside itself.
def avrg(*args):
    total = 0
    for num in args:
        total += num
    return total / len(args)
print(avrg(2,3,5,6))
# %%
