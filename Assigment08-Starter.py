# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Ehren Williamson,03/03/2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:



    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Ehren Williamson,03/03/2021,Modified code to complete assignment 8
    """
    def __init__(self, product_name, product_price): 
        self.product_name = product_name
        self.product_price = product_price

    @property
    def product_name(self):
        return self.__product_name
        
    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = product_name
    
    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, product_price):
        self.__product_price = product_price

    def __str__(self):
        return self.product_name +"," + str(self.product_price)

    def __doc__():
        print("creates a Product with product name and price with setters and getters")

    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    def save_data_to_file(file_name,list_of_product_objects):
        file = open(file_name, "w")
        for item in list_of_product_objects:
            file.write(str(item)+ "\n")

        file.close()
        return "Success"

    def read_data_from_file(file_name):
        file = open(file_name, "r")
        for item in file:
            productSplit = item.split(",")
            addingProduct = Product(productSplit[0],productSplit[1])
            lstOfProductObjects.append(addingProduct)
        file.close()
     def __doc__():
        print("Very simple class that takes in a file name and/or list of product objects and does read/write operations")
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) See current names and prices
        2) Add product names and prices
        3) Save products       
        4) Exit program
        ''')
        return 
    def get_user_choice():
        choice = input("please choose an option[1-4]:")
        return choice

    def show_data_from_file(file_name):
        lstdata = FileProcessor.read_data_from_file(file_name)
        for item in lstdata:
            print(item)

    def get_product_data():
        
        product_name = input("What is the product name?")
        product_price = float(input("What is the product price?"))
        newProduct = Product(product_name,product_price)
        return newProduct
        
     def __doc__():
        print("Creates IO functionality to make the main script easier to read")
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
FileProcessor.read_data_from_file(strFileName)
IO.print_menu_tasks()
choices = IO.get_user_choice()

while(True):
    if choices == "1":
        for item in lstOfProductObjects:
            print(item)
        IO.print_menu_tasks()
        choices = IO.get_user_choice()
    elif choices == "2":
        addProduct = IO.get_product_data()
        lstOfProductObjects.append(addProduct)
        IO.print_menu_tasks()
        choices = IO.get_user_choice()
    elif choices == "3":
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        print("Save Successful have a great day")
        break
    elif choices == "4":
        print("Have a great Day")
        break 
    else:
        print("Not a valid selection")
        IO.print_menu_tasks()
        choices = IO.get_user_choice()


