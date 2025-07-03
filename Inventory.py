#BSCIT-05-0836/2022
#Inventory Management System
def inventory_system():

# Dictionary to store item names and their quantities
    stock = {}

# Function to display the main menu options
    def menu():
        print("\n...Inventory Management...")
        print("1. Add or Update Item")
        print("2. Search for an Item")
        print("3. Display All Items")
        print("4. Quantity in Inventory")
        print("5. Exit")
        print("................................")
        
# Function to add a new item or update quantity of existing item
    def add_update_item():
        item_name = input("Enter item name:").strip()
        try:
            count = int(input(f"Enter quantity for {item_name}:"))
            if count<0:
                print("Quantity cannot be negative.")
                return

# If item exists, show updated message
            if item_name in stock:
                print(f"{item_name} already exists. Update quantity from {stock[item_name]} to {count}.")
            else:
                print(f"{item_name} added to inventory with {count} units.")
            stock[item_name]=count
        except ValueError:
            print("Invalid quantity input. Please enter a number.")
            
# Function to search for an item in the inventory            
    def lookup_item():
        name = input("Enter item name to search:").strip()
        if name in stock:
            print(f"{name}:{stock[name]} units available.")
        else:
            print(f"{name} is not in the inventory.")
            
# Function to list all items currently in the inventory            
    def list_all_items():
        if not stock:
            print("No items in inventory.")
        else:
            print("\nInventory Contents:")
            for item, qty in stock.items():
                print(f"{item}: {qty} units")
                
# Function to calculate and display total number of units in inventory               
    def calculate_total():
        total_items = sum(stock.values())
        print(f"\nTotal number of units in inventory:{total_items}")
        
# Main loop to keep showing menu and process user input        
    while True:
        menu()
        selection = input("Choose an option (1-5):").strip()

        if selection == '1':
            add_update_item()
        elif selection == '2':
            lookup_item()
        elif selection == '3':
            list_all_items()
        elif selection == '4':
            calculate_total()
        elif selection == '5':
            print("Closing inventory system. Have a great day!")
            break
        else:
            print("Invalid choice. Please pick a number between 1 and 5.")
            
if __name__ == "__main__":
    inventory_system()
