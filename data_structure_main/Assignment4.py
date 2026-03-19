## TASK -1
sales =[1200,450,980,1500,3000]

f=open('sales_data.txt','w')

for s in sales:
    f.write(str(s)+"\n")

f.close()

f=open('sales_data.txt','r')
print(f.read())

f.close()



## TASK -2
# Reading entire file using read()
f=open("sales_data.txt","r")
data =f.read()
print("Using read():", data)
f.close()

#reading first line using readline()
f=open("sales_data.txt","r")
first_line =f.readline()
print("Using readline():", first_line)
f.close()

# reading all lines using readlines()
f=open("sales_data.txt","r")
lines =f.readlines()
sales_list = []
for line in lines:
    sales_list.append(int(line.strip()))   # remove \n and convert to int

print("Using readlines():")
print(sales_list)

f.close()



### TASK -3
new_sales =[5000,2500,1700]
f= open("sales_data.txt","a")  # open in append mode
for s in new_sales:
    f.write(str(s)+"\n")

f.close()

# printing the updated sales
f=open("sales_data.txt","r")
print("Updated sales data:")
print(f.read())
f.close()

# counting total lines after updating 
f =open("sales_data.txt","r")
line = f.readlines()
print("Total number of lines:", len(line))
f.close()



# TASK -4
f = open("sales_data.txt","r")
lines = f.readlines()

sales = []
for line in lines:
    sales.append(int(line.strip()))
f.close()

# calculating values 
total_sales = sum(sales)
highest_sales = max(sales)
lowest_sales = min(sales)
average_sales = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Average Sales:", average_sales)



## TASK -5
f =open("products.txt","w")

for i in range(3):
    name = input("Enter product name:")
    price = input("Enter product price:")

    f.write(name + "|" + price + "\n")

f.close()

f =open("products.txt","r")
lines = f.readlines()

print("\n Product List:")
for line in lines:
    product, price = line.strip().split("|")
    print(f"Product: {product}, Price: {price}")

f.close()



## TASK -6
import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    f = open(filename, "r")
    print(f.read())
    f.close()
else:
    print("File not found. Please check the filename.")



## TASK - 7
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

f = open("discount_report.txt", "w")

f.write("Product | Original Price | Discounted Price\n")

# initialize variables BEFORE loop
total_discounted = 0
count = 0

for product, price in prices.items():

    discounted_price = price - (price * discount / 100)

    f.write(product + " | " + str(price) + " | " + str(discounted_price) + "\n")

    total_discounted += discounted_price
    count += 1

avg_discounted = total_discounted / count

f.write("\nTotal Items: " + str(count) + "\n")
f.write("Average Discounted Price: " + str(avg_discounted))

f.close()

f = open("discount_report.txt", "r")
print(f.read())
f.close()
