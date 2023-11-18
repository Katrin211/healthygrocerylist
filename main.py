from healthy_grocery_list import HealthyGroceryList

# Create an instance of the HealthyGroceryList class
grocery_list = HealthyGroceryList()

# User input for the grocery list
print("Enter your grocery list. Type 'done' when finished.")
while True:
    category = input("Enter the category (protein, vegetable, fruit, healthy fat, legume, carbohydrate, drink): ")
    if category.lower() == "done":
        break

    item = input("Enter the item: ")
    grocery_list.add_to_list(category, item)

# Check the healthiness of the grocery list
if grocery_list.check_healthiness():
    print("Your grocery list meets the conditions for a healthy lifestyle!")
else:
    print("Your grocery list does not meet all the conditions for a healthy lifestyle.")

