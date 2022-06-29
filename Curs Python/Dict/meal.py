from content import pantry, recipes

def add_shopping_item(data: dict, item: str, amount: int):
    """Add a tuple containing items and data"""
    data[item] = data.setdefault(item, 0) + amount
    
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
    
shopping_list = {}
   
while True:
    print("")
    print("Please choose your recipes")
    print("------------------------")
    for key, value in display_dict.items():
        print(f"{key}-{value}")
        
    choice = input(": ")
    if choice == 0:
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selcted {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity = pantry.get(food_item, 0)
            if required_quantity <= quantity:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity
                print(f"You need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity)

for things in shopping_list.items():
    print(things)