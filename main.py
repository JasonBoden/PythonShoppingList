import sys

# Create the main menu
def mainMenu():
	while True:
		print()
		print('''### SHOPPING LIST ###
		
			Select a number for the action that you would like to do:
		
			1. View the shopping list
			2. Add item to shopping list
			3. Remove item from shopping list
			4. Check if item is on shopping list
			5. How many items on shopping list
			6. Clear shopping list
			7. Exit
			''')

		selection = input("Make your selection: ") # Ask the user to make a selection

		if selection == "1":
			displayList()
		elif selection == "2":
			addItem()
		elif selection == "3":
			removeItem()
		elif selection == "4":
			checkItem()
		elif selection == "5":
			listLength()
		elif selection == "6":
			clearList()
		elif selection == "7":
			sys.exit("you are exiting the shopping list!")
		else:
			print("You did not make a valid selection.")

shopping_list = ["apples", "bananas", "carrots", "potatoes"] # Added some items to shopping list to begin
# Displays all items on the shopping list
def displayList():
	print()
	print("--- SHOPPING LIST ---")
	for i in shopping_list:
		print("*" + i)

# Adds an item to the shopping list
def addItem():
	item = input("Enter the item you wish to add to the shopping list: ")
	shopping_list.append(item)
	print(item, "has been added to the shopping list")

# Removes an item from the shopping list
def removeItem():
	item = input("Enter the item you wish to remove to the shopping list: ")
	shopping_list.remove(item)
	print(item, "has been removed to the shopping list")

# Checks if an item is on the shopping list
def checkItem():
	item = input("What item would you like to check? ")
	if item in shopping_list:
		print(f"Yes, {item} is on the shopping list")
	else:
		print(f"{item} is not on the shopping list!")

# Tells the user how many items are on the shopping list
def listLength():
	print("There are", len(shopping_list), "items on the shopping list.")

# Removes all items from the shopping list
def clearList():
	shopping_list.clear()
	print("Your shopping list is now empty!")

# Run the function mainMenu - which will run our app
mainMenu()