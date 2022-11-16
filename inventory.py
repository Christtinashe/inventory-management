
#program for managing  stock at a nike warehouse
# creating a class called shoe
class Shoe:

    # creating a constructor method with parameters, self, country, code, product, cost, quantity.

    def __init__(self, country, code, product, cost, quantity):
    
      # creating  Attributes within our class Shoe.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Create a method called gett cost to return self.cost
    def get_cost(self):
        return self.cost

    # Create a method called file_updated that returns attributes within shoe class
    def file_updated(self):
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''

    # Create a methos called get_quantity to return self.quantity

    def get_quantity(self):
        return self.quantity
    
    
#string methond to return format of parameters when printed out
    def __str__(self):
        return (f'''\nCountry:{self.country}
Shoe Code: {self.code}
Shoe Name: {self.product}
Shoe Cost: {self.cost}
Quantity: {self.quantity}\n''')


#open shoe list where list items will be appended
shoe_list = []


# We create a function called read_shoes_data.
def read_shoes_data():
     
    try:
        # We then also open our textfile called inventory.txt and read all the lines from it.
        with open('inventory.txt', 'r') as shoes_in_inventory:
            file_shoe_list = shoes_in_inventory.readlines()
        
        #for loop to iterate through the list and calculate len of list to show contents of inventory
        for line in range(1, len(file_shoe_list)):
        
                #strip file to remove any new lines
                #split after it has converted to a list
                country, code, product, cost, quantity = file_shoe_list[line].strip('\n').split(',')

                # creating an object named inv_shoes to call shoe class 
                inv_shoes = Shoe(country,code,product,float(cost),int(quantity))
                # Then we append shoes to our list shoe_list.
                shoe_list.append(inv_shoes)
    #exeption if user types wrong text file name
    except FileNotFoundError:
        print('inventory file not found. Please check file name correctly')
      

read_shoes_data()
   

#a function called capture shoes that captures all the invetory shoes
def capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity):
    #captured shoes object to show all captured shoes and appends the shoes to shoe list
    captured_shoes = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)
    # appending to our shoe_list.
    shoe_list.append(captured_shoes)
   

#update function to update quantity once
def update():

    # Create a variable called obj_data.
    # This will take my intake my shoe objects.

    obj_data = f'Country,Code,Product,Cost,Quantity'

    # Create a for loop for the to iterate over the shoe list.
    
    for shoe in shoe_list:
        obj_data += '\n' + shoe.file_updated()

    # We then open our file and write to it.

    with open('inventory.txt', 'w') as shoe_list_inventory:
        shoe_list_inventory.write(obj_data)  

#view all function to view all shoes in shoe list
def view_all():
    print(*shoe_list)


# deock to re stock inventory
def re_stock():

    # We create a variable called qty(quantity) initialse it to shoe_list index 0.
    # We then create a counter called shoe_index intialise it to 0.

    qty = shoe_list[0].quantity
    shoes_index = 0

    # Then we set variable qty to our method.
     # Then we make a for loop and use enumerate to iterate our shoe list.
    for i, s in enumerate(shoe_list):
        if s.get_quantity() < qty:
          qty = s.quantity
          shoes_index = i

    # Then we return the shoe_index.

    return shoes_index
  

#function to search for a shoe using code
def search_shoe(s_code):
   
    # for loop to find code of shoes
    for shoe_code in shoe_list:
        if shoe_code.code == s_code:
            # if its eqauls to the parameter from the users input.
            return shoe_code 
    # if not found then return that the shoe code is not found.
    return f'The shoe code {s_code} is not found\n'
    

#funtion to find vale per item
def value_per_item():
    # We create a for loop to iterate through the shoe_list.
    for s in shoe_list:
        # We then create our calculation.
        value = s.cost * s.quantity
        #printing value per item
        print(f'{s}Value: {value}\n')



#funtion to find highest quantity
def highest_qty():
    shoe_index = 0
    maximum_quantity = shoe_list[shoe_index].get_quantity()

    #for loop to iterate through shoe list
    for s, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > maximum_quantity:
            maximum_quantity = shoe.get_quantity()
            shoe_index = s

    # print the sale and the shoe_list[shoe_index].
    print(f'Sale Sale , shoe is on sale {shoe_list[shoe_index]}\n')

def exit():
    print('thank you for stock taking we appreciate everything you do for this company')

    


# creating logic

user_choice = ''' '''


#while loop to  begin logic with user choice menu
while user_choice != 'end stock taking':
    user_choice = input('''\nPlease view below and select
    c = Capture data about a shoe
    v = This will view all the shoes
    r = Find shoe that needs to be restocked
    f = This will search for a shoe
    v = Calculate the total value
    s = Shoe on sale
    e = stop stock taking \n''').lower()

    # if statement if chois to capture shoes
    if user_choice == 'c':
        #asking user shoe details
        shoe_country = input('Please enter the country of the shoes ')
        shoe_code = input('Please enter the shoe code ')
        shoe_name = input('Please enter product name ')
        shoe_cost = float(input('Please enter the cost of the shoe ')) 
        shoe_quantity = int(input('Please enter the quantity of the shoes '))
        #calling capture shoes function to capture shoe from user input
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity )


     #elif statement if user wants to view shoes and all its details in inventory
    elif user_choice == 'v':
        view_all()

    
    #elif statement  if employee wants to restock
    elif user_choice == 'r':
        #calling restock function
        shoe_index = re_stock()
    
        # printing shoe to be restocked
        print(f' This is the shoe with the lowest quantity from all your stocking {shoe_list[shoe_index]} ')
        restock_choice = input('''Please see the quantity above and advise if you will be restocking
Please choose:
Yes - for the restock
No -  for not restocking \n''')
        

        #if user chosees to restock
        if restock_choice == 'yes':
            shoe_list[shoe_index].quantity = int(input('Please enter new quantity number: \n'))
    
    # logic if user does not want to restock
        if restock_choice == 'no':
            print('Quantity will remain the same\n')

        #calling funtions to update and re-stock
        update()
        re_stock()
       
        
    #elif statement if user wants to find shoe
    elif user_choice == 'f':
        s_code = input('Please enter the shoe code you looking for: ')
        #printing shoe details according to serch code
        print(f'{search_shoe(s_code)}')
        
    
    #elif statement if user wants to check value of item
    elif user_choice == 'v':
        value_per_item()
    

    #elif to find highest quaunty and put shoe on sale
    elif user_choice == 's':
        highest_qty()

    
    #elif statement if user wants to stop stock taking
    elif user_choice == 'e':
        print('print goodbye')
        exit()
        break
    

    #asking user to restatr if incorrect input inserted 
    else:
        print('Please select correctly what you would like to do.')