#     TASK 1

# 1. Create a list of products
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor",]

# 2. Create a tuple for a sample product (name, price, category)
sample_product = ("Laptop", 80000, "Electronics")

# 3. Print the 2nd and last product
print("2nd product:", products[1])
print("Last product:", products[-1])
print("The 2nd and Last products:", products[1:7:3])  # Slicing the list to get the 2nd and last product

#4 Appending the list with two new product
products.append("Printer")
products.append("Webcam")
# updated list 
print("Updated products list:", products)

# converting tuple to list
sample_product_list = list(sample_product)
sample_product_list[1] = 90000  # Update the price in the list
sample_product_list = tuple(sample_product_list)  # Convert back to tuple
print("Updated sample product tuple:", sample_product_list)


#    TASK 2

# Products list (from Task 1)
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]

# 1. Parallel list of categories (same length as products)
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics"
]
# Create a set of categories
categories_set = set(categories)
print("Initial categories set:", categories_set)

# 2. Add a new category and try adding a duplicate
categories_set.add("Office")
categories_set.add("Electronics")  # duplicate, will be ignored

print("Categories after adding:", categories_set)

# 3. Checking if a category exists
print("Is 'Accessories' in categories_set?", "Accessories" in categories_set) # The ans is in Boolean

# Extra 
# Total number of unique categories
print("Total unique categories:", len(categories_set))


#    TASK 3

# 1. Create a price dictionary
price_dict= {
    "Laptop": 80000,
    "Smartphone": 50000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
    }

# 2. Add a new product
price_dict["Webcam"] = 3000
print(price_dict)

# Update price of an existing product
price_dict["Mouse"] = 900

# Remove a product safely
product_to_remove = "Printer"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove, "not found in price list")

# Extra 
# Printin the Product with both maximum and minimum price
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Product with maximum price:", max_product,"->" "Price:", price_dict[max_product])
print("Product with minimum price:", min_product,"->""Price:", price_dict[min_product])


# TASK 4

products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics"
]
price_dict= {
    "Laptop": 80000,
    "Smartphone": 50000,                    
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
    }
# 1. Create a list of tuples (product, category, price)
catalog = []

for i in range(len(products)):
    product = products[i]
    price = price_dict[product]
    category = categories[i]
    catalog.append((product, price, category))
print("Product Catalog :", catalog)

# 2. Create category_to_products dictionary
category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)
print("Category to Products Dictionary:", category_to_products)

#3. Print products from category with maximum products
max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
print("Category with maximum products:", max_category)
print("Products in this category:", category_to_products[max_category])