 # TASK 1
 order_amount = input("Enter the order amount: ")

#checking if input is numeric
if order_amount.isdigit():
    order_amount= int (order_amount)

    # Applying discounts rules 

    if order_amount >= 2000:
        discount =0.15
    elif order_amount >=1500 :
        discount = 0.10
    elif order_amount >=1000 :
        discount = 0.07
    else:
        discount = 0.0

    # calculating discount 
    discount_amount = order_amount *discount
    subtotal = order_amount - discount_amount

    # Add 5% tax
    tax = subtotal*0.05
    final_total = subtotal+tax

    print("Original Amount:",order_amount)
    print("Discount Amount:",discount_amount)
    print("Amount after discount:",subtotal)
    print("Tax(5%):", tax)
    print("Final Total:", final_total)
else:
    print("Error: Please enter a valid numeric value.")



# TASK 2

orders = [1200, 2500,800,1750,3000]

total_revenue =0
discount_order_count =0
print ("Order Amount -> Discount % -> Final Amount")
print("------------------------------------------------")

for order_amount in orders:

    # Applying discounts rules 

    if order_amount >= 2000:
        discount =0.15
    elif order_amount >=1500 :
        discount = 0.10
    elif order_amount >=1000 :
        discount = 0.07
    else:
        discount = 0.0

    discount_amount = order_amount *discount
    final_amount = order_amount - discount_amount

    # Add to total revenue
    total_revenue= total_revenue+final_amount

        # count discount order 
    if discount>0:
        discount_order_count= discount_order_count+1

        # print summery row 
    print(order_amount,"->", discount*100,"%->",final_amount)

print("----------------------------------------------------")
print("Total Revenue After Discount :",total_revenue)
print("Number od Orede with DIscount :", discount_order_count)



# TASK 3

orders = []

while True:

    print("\n===== ORDER MENU =====")
    print("1 - Add Order Amount")
    print("2 - Show Orders and Totals After Discount")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "q":
        print("Exiting program...")
        break

    elif choice == "1":
        amount = input("Enter order amount: ")

        if amount.isdigit():
            orders.append(int(amount))
            print("Order added successfully.")
        else:
            print("Invalid amount! Please enter a numeric value.")
            continue

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total_revenue = 0   

        print("\nOrder  ->  Discount %  ->  Final Amount")
        print("----------------------------------------")

        for order_amount in orders:

            if order_amount >= 2000:
                discount = 0.15
            elif order_amount >= 1500:
                discount = 0.10
            elif order_amount >= 1000:
                discount = 0.07
            else:
                discount = 0.0

            discount_amount = order_amount * discount
            final_amount = order_amount - discount_amount

            total_revenue = total_revenue + final_amount

            print(order_amount, " -> ", discount * 100, "%  -> ", final_amount)

        print("----------------------------------------")
        print("Total Revenue After Discounts:", total_revenue)

    else:
        print("Invalid choice! Please select 1, 2, or q.")
        continue



# TASK 5
daily = [200, 150, 0, 400, 50, -1,300]
total_sales = 0

for day in daily:
    # if day is negative, it indicates corrupted data
    if day ==-1:
        print("Corrupted data detected, Stopping processing,")
        break
    # if day is zero, it indicates no sales for that day, we can skip it
    elif day == 0:
        print("No sales for this day, skipping.")
        continue
    else:
        total_sales = total_sales + day
        print("Added:", day, "Running Total:", total_sales)
print("Total Sales:", total_sales)

