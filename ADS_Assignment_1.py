#Algorithms and Data Structures Assignment 1
#Quincy Chan, 100894159
import time
#loading the products
products = []
def loadProductData():
    textFile = "product_data.txt"
    
    with open(textFile, 'r') as file:
    #set empty array
        for line in file:
            #split items with comma
            data = line.strip().split(',')
            product = {
                'ID': data[0],
                'Name': data[1],
                'Price': data[2],
                'Category': data[3]
            }
            #adds the entries to the empty array          
            products.append(product)
    return products

#Operation 1. this function prints all the data in the same format as the text file: ID, name, price, category
def dataLoad():
    #products = loadProductData()
    for product in products:
        print(f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}")

#Operation 2: this function lets user add new product entry
def insert():
    id = input("Enter the ID: ")
    name = input("Enter the name: ")
    price = input("Enter the price: ")
    category = input("Enter the category: ")
    product = {
        'ID': id,
        'Name': name,
        'Price': price,
        'Category': category
    }
    products.append(product)
    print("You have added the product!")
    
#Operation 3: this function lets user update existing product details
def update():
    id = input("Enter the product ID that you want to edit: ")
    status = False
    #checks if ID entered matches ID in the data entry, if match then status = true and will prompt user to enter the updating data
    for product in products:
        if product["ID"] == id:
            status = True
            print("The item you searched for exists. Enter the updated data: ")
            product['Name'] = input("Enter updated name: ")
            product['Price'] = input("Enter updated Price: ")
            product['Category'] = input("Enter updated Category: ")
            print("Your product has been updated!")
            break
    if not status:
        print("The ID you have entered does not exist!")
        
#Operation 4: this function lets user delete products by entering it's ID. Program will find the match and delete that entry.
def delete():
    id = input("Enter the product's ID you want to delete: ")
    #default status is false for match
    status = False
    #if matches, then program will delete the entry with the matching product ID
    for product in products:
        if product['ID'] == id:
            status = True
            products.remove(product)
            print("The product with the matching ID entered has been deleted.")
            break
    #if no match then prints an error
    if not status:
        print("Error: the product ID you searched is not found.")
            
#Operation 5: this function lets the user search for an ID of a product and the program will display it in print.
def search():
    searchId = input("Enter the product's ID that you want to find: ")
    status = False
    for product in products:
        status = True
        print("The product has been found!")
        print(f"{product['ID']}")
        print(f"{product['Name']}")
        print(f"{product['Price']}")
        print(f"{product['Category']}")
        break
    #if no match then prints an error
    if not status:
        print("Error: the product ID you searched is not found.")
        
#Operation 6: this function lets user sort the data in the text file using bubble sort
def bubbleSort():
    n = len(products)
    #we make a copy of the list in its original order
    productsCopy = products[:]
    #Measure the time for the sort to complete
    #Start time
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            #compares the first 2 elements, and if FIRST element is greater than SECOND element, swap them
            #continue until all the Prices have been numerically sorted from least to greatest.
            if float(products[j]['Price']) > float(products[j + 1]['Price']):
                products[j], products[j + 1] = products[j + 1], products[j]
    #End time
    end = time.time()
    print("\nThe products have been sorted using bubble sort! Average Case O(n^2)")
    for product in products:
        print(f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}")
    #Calculates the total time taken to complete the sort
    totalTime = end - start
    #Average case: O(n^2)
    print("\nThe total time for Average Case is: {:.30f} seconds".format(totalTime))
    print("----------------------------------------------------------------------------------")
    
    #------------------------------------------------------------------------------------------
    #Best Case: O(n)
    productsSorted = sorted(products, key=lambda x: float(x['Price']))
    for product in productsSorted:
        print(f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}")
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            #compares the first 2 elements, and if FIRST element is greater than SECOND element, swap them
            #continue until all the Prices have been numerically sorted from least to greatest.
            if float(products[j]['Price']) > float(products[j + 1]['Price']):
                products[j], products[j + 1] = products[j + 1], products[j]
    end = time.time()
    #Calculates the total time taken to complete the sort
    totalTime = end - start
    print("\nSorting the list in already sorted order! Best Case O(n)")
    print("The total time for Best Case is: {:.30f} seconds".format(totalTime))
    print("----------------------------------------------------------------------------------")
    
    #-------------------------------------------------------------------------------
    #Worst Case: O(n^2)
    print("\nThis is bubble sorting the list in reverse: ") 
    #we reverse it's order so it becomes reversed list
    productsReverse = sorted(products, key=lambda x: float(x['Price']), reverse=True)
    for product in productsReverse:
        print(f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}")
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            #compares the first 2 elements, and if FIRST element is greater than SECOND element, swap them
            #continue until all the Prices have been numerically sorted from least to greatest.
            if float(products[j]['Price']) > float(products[j + 1]['Price']):
                products[j], products[j + 1] = products[j + 1], products[j]
    end = time.time() 
    #Calculates the total time taken to complete the sort
    totalTime = end - start
    #Average case: O(n^2)
    print("\nThe list is sorted in reverse order! Worst Case O(n^2)")
    print("The total time for Worst Case is: {:.30f} seconds".format(totalTime))
    print("----------------------------------------------------------------------------------")

#---------------------------------------------------------
#call the functions
#prompts the user to enter an operation
loadProductData()
while True:
    print("------------------------------------------------")
    print("Option 1: Load Data")
    print("Option 2: Insert")
    print("Option 3: Update")
    print("Option 4: Delete")
    print("Option 5: Search")
    print("Option 6: Sort and Display Time")
    print("------------------------------------------------")
    prompt = input("Please enter an Operation (1-6): ")
    #user's choices
    if prompt == '1':
        dataLoad()
    elif prompt == '2':
        insert()
    elif prompt == '3':
        update()
    elif prompt == '4':
        delete()
    elif prompt == '5':
        search()
    elif prompt == '6':
        bubbleSort()
    else:
        print("Error, not a valid option")