# Online Shopping Order Management System

customers = []


def add_customer():
    customer = {}
    customer["CustomerId"] = int(input("Enter Customer ID: "))
    customer["CustomerName"] = input("Enter Customer Name: ")
    customer["City"] = input("Enter City: ")
    customer["Orders"] = []

    customers.append(customer)
    print("Customer added successfully.")


def add_product():
    cid = int(input("Enter Customer ID: "))
    found = False

    for customer in customers:
        if customer["CustomerId"] == cid:
            product = {}
            product["ProductId"] = int(input("Enter Product ID: "))
            product["ProductName"] = input("Enter Product Name: ")
            product["Quantity"] = int(input("Enter Quantity: "))
            product["Price"] = float(input("Enter Price: "))

            customer["Orders"].append(product)
            print("Product added successfully.")
            found = True
            break

    if found == False:
        print("Customer not found.")


def view_customers():
    if len(customers) == 0:
        print("No customer records found.")
    else:
        for customer in customers:
            print("\nCustomer ID :", customer["CustomerId"])
            print("Customer Name :", customer["CustomerName"])
            print("City :", customer["City"])

            print("\nOrders")
            if len(customer["Orders"]) == 0:
                print("No Orders.")
            else:
                for product in customer["Orders"]:
                    print("\nProduct ID :", product["ProductId"])
                    print("Product Name :", product["ProductName"])
                    print("Quantity :", product["Quantity"])
                    print("Price :", product["Price"])

            print("----------------------------------------")


def search_customer():
    cid = int(input("Enter Customer ID: "))
    found = False

    for customer in customers:
        if customer["CustomerId"] == cid:
            print("\nCustomer ID :", customer["CustomerId"])
            print("Customer Name :", customer["CustomerName"])
            print("City :", customer["City"])

            print("\nOrders")
            if len(customer["Orders"]) == 0:
                print("No Orders.")
            else:
                for product in customer["Orders"]:
                    print("\nProduct ID :", product["ProductId"])
                    print("Product Name :", product["ProductName"])
                    print("Quantity :", product["Quantity"])
                    print("Price :", product["Price"])

            found = True
            break

    if found == False:
        print("Customer not found.")


def update_quantity():
    cid = int(input("Enter Customer ID: "))
    pid = int(input("Enter Product ID: "))
    found = False

    for customer in customers:
        if customer["CustomerId"] == cid:
            for product in customer["Orders"]:
                if product["ProductId"] == pid:
                    qty = int(input("Enter New Quantity: "))
                    product["Quantity"] = qty
                    print("Quantity updated successfully.")
                    found = True
                    break
            break

    if found == False:
        print("Customer or Product not found.")


def remove_product():
    cid = int(input("Enter Customer ID: "))
    pid = int(input("Enter Product ID: "))
    found = False

    for customer in customers:
        if customer["CustomerId"] == cid:
            for product in customer["Orders"]:
                if product["ProductId"] == pid:
                    customer["Orders"].remove(product)
                    print("Product removed successfully.")
                    found = True
                    break
            break

    if found == False:
        print("Customer or Product not found.")


def total_bill():
    cid = int(input("Enter Customer ID: "))
    found = False

    for customer in customers:
        if customer["CustomerId"] == cid:
            total = 0
            print()

            for product in customer["Orders"]:
                amount = product["Quantity"] * product["Price"]
                print(product["ProductName"], ":", amount)
                total = total + amount

            print("------------------------")
            print("Total Bill :", total)
            found = True
            break

    if found == False:
        print("Customer not found.")


def max_order_value():
    if len(customers) == 0:
        print("No customer records found.")
    else:
        max_customer = None
        max_total = 0

        for customer in customers:
            total = 0
            for product in customer["Orders"]:
                total += product["Quantity"] * product["Price"]

            if total > max_total:
                max_total = total
                max_customer = customer

        if max_customer != None:
            print("\nCustomer Name :", max_customer["CustomerName"])
            print("Total Amount :", max_total)


while True:
    print("\n========== Online Shopping Order Management System ==========")
    print("1. Add New Customer")
    print("2. Add Product Order")
    print("3. View All Customers and Their Orders")
    print("4. Search Customer")
    print("5. Update Product Quantity")
    print("6. Remove Product")
    print("7. Calculate Total Order Value")
    print("8. Display Customer with Maximum Order Value")
    print("9. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_customer()

    elif choice == 2:
        add_product()

    elif choice == 3:
        view_customers()

    elif choice == 4:
        search_customer()

    elif choice == 5:
        update_quantity()

    elif choice == 6:
        remove_product()

    elif choice == 7:
        total_bill()

    elif choice == 8:
        max_order_value()

    elif choice == 9:
        print("Thank you for using Online Shopping Order Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")