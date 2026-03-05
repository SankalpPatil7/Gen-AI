## TASK - 1

def apply_discount(price, discount_percentage=5):
    # ensureing discount does not exceed 60%
    if discount_percentage > 60:
        discount_percentage = 60

    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount

    return final_price
#Test case 
print("Price after default discount:", apply_discount(500)) # uses default 5% discount
print("Price after 10% discount:", apply_discount(500, 10)) 



# TASK - 2
def factorial(n):
   if n < 0:
       return "Error: Factorial is not defined for negative numbers."
   elif n == 0 or n == 1:
       return 1
   else:
       return n * factorial(n-1)

# Test case
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))


#TASK - 3

gst = lambda price:price + (0.18*price)
print("Price after GST:", gst(100))

#EXTRA TASKS
final_price = lambda price, discount: (price + 0.18 * price) - ((price + 0.18 * price) * discount / 100)
print("Price after GST and 10% discount:", final_price(100, 10))



# TASK - 4
prices=[100,250,400,1200,50]
print("Original Prices:", prices)
prices_with_gst= list(map(lambda price: price + (0.18 * price), prices))
print("Prices after GST:", prices_with_gst)



# TASK - 5
prices=[100,250,400,1200,50,2000,850]
filtered_prices = list(filter(lambda price: price > 500, prices))
print("Prices greater than 500:", filtered_prices)
filtered_prices_less_than_500 = list(filter(lambda price: price < 500, prices))
print("Prices less than 500:", filtered_prices_less_than_500)



# TASK - 6
def process_prices(prices):
    discounted_price =list(map(lambda price: price - (0.10 * price), prices))
    print(discounted_price)
    filtered_prices = list(filter(lambda price: price >300, discounted_price))
    print(filtered_prices)
process_prices([100,500,900,50,750])



# TASK -7

def add_price(prices_list, price):
    prices_list.append(price)
    
def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return None
    return max(prices_list)

#menu 
prices = []
while True:
    print("\nMenu:")
    print("1 - Add Price")
    print("2 - Get Average Price")
    print("3 - Get Maximum Price")

    choice = input("Enter your choice: ")
    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices, price)

    elif choice == "2":
        avg = get_average_price(prices)
        print("Average price:", avg)

    elif choice == "3":
        highest = get_max_price(prices)
        print("Highest price:", highest)

    elif choice == "q":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


