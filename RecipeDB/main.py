import sqlite3

def show_menu():
   print("\n\nPlease select an option:")
   print(" 1) See Recipes")
   print(" 2) Add Recipe")
   print(" 3) Edit Recipe")
   print(" 4) Delete Recipe")
   print(" 5) Quit")

def get_input_list_str_with_prompt(prompt):
    resp = " "
    list_str = ""
    print(prompt)
    while resp.lower() != "":
        resp = input("> ")

        if resp.lower() != "":
            seperator = ",,," if list_str != "" else ""
            list_str += f"{seperator}{resp}"
    return list_str

def main():
    conn = sqlite3.connect('test.db')
    choice = 0

    # Create the table if it doesn't already exist
    conn.execute('''CREATE TABLE IF NOT EXISTS RECIPES
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                RECIPE_NAME      TEXT   NOT NULL,
                INGREDIENTS      TEXT   NOT NULL,
                INSTRUCTIONS     TEXT   NOT NULL);''')

    print("\nWelcome to RecipeDB!")
    while choice < 5:
        choice = 0
        show_menu()

        while choice == 0:
            resp = input("> ")

            if resp.isnumeric():
                resp = int(resp)
                if resp > 0 and resp < 6:
                    choice = resp
                else:
                    print("Please enter a number 1-5")
            else:
                print("Please enter a number 1-5")
        
        if choice == 2:
            rname = input("\nWhat is the name of the recipe?\n> ")
            ingredients = get_input_list_str_with_prompt("\nWhat are the ingredients? (add one at a time,  hit enter to stop)")
            instructions = get_input_list_str_with_prompt("\nWhat are the instructions? (add one at a time,  hit enter to stop)")

            conn.execute(f"INSERT INTO RECIPES (RECIPE_NAME,INGREDIENTS,INSTRUCTIONS) \
                  VALUES ('{rname}', '{ingredients}', '{instructions}' )")
            conn.commit()
            input("Recipe added! (press enter to continue)")
        elif choice < 5:
            print()
            recipe_cursor = conn.execute("SELECT id, recipe_name, ingredients, instructions from RECIPES")
            recipe_rows = recipe_cursor.fetchall()
            chosen_id = -1
            if len(recipe_rows) > 0:
                for row in recipe_rows:
                    print(f"{row[0]}) {row[1]}")
                print("\nEnter the ID of the recipe you wish to select, or 0 to exit")

                while chosen_id < 0:
                    new_id = input("> ")
                    if new_id.isnumeric():
                        new_id = int(new_id)
                        if new_id == 0:
                            chosen_id = new_id
                        else:
                            selected_cursor = conn.execute(f'''SELECT ID FROM RECIPES WHERE ID={new_id};''')
                            if len(selected_cursor.fetchall()) > 0:
                                chosen_id = new_id
                            else:
                                print("Please enter a valid ID")
                    else:
                        print("Please enter a valid ID")
            else:
                input("No recipes to show. Press enter to contiue.")

            chosen_recipe = conn.execute(f'''SELECT ID, RECIPE_NAME, INGREDIENTS, INSTRUCTIONS FROM RECIPES WHERE ID={chosen_id};''')
            for row in chosen_recipe:
                print(f"\n{row[1]}")
                print("\nIngredients:")
                for ingredient in row[2].split(",,,"):
                    print(f"- {ingredient}")
                print("\nInstructions:")
                for instruction in row[3].split(",,,"):
                    print(f"- {instruction}")

                if choice == 1:
                    input("\nPress enter to exit.")
                elif choice == 3:
                    rname = row[1]
                    ingredients = row[2]
                    instructions = row[3]
                    edit_choice = 0

                    while edit_choice < 4:
                        print("Select the following to edit:")
                        print(" 1) Recipe Name")
                        print(" 2) Ingredients")
                        print(" 3) Instructions")
                        print(" 4) Exit")
                        edit_choice = 0

                        while edit_choice == 0:
                            e_choice = input("> ")

                            if e_choice.isnumeric():
                                e_choice = int(e_choice)
                                if e_choice > 0 and e_choice < 5:
                                    edit_choice = e_choice
                                else:
                                    print("Please enter a number 1-4")
                            else:
                                print("Please enter a number 1-4")

                        if edit_choice == 1:
                            rname = input("\nWhat would you like the new name of the recipe to be?\n> ")
                        elif edit_choice == 2:
                            ingredients = get_input_list_str_with_prompt("\nWhat is the new list of ingredients? (add one at a time, hit enter to stop)")
                        elif edit_choice == 3:
                            instructions = get_input_list_str_with_prompt("\nWhat is the new set of instructions? (add one at a time, hit enter to stop)")
                        
                    conn.execute(f"UPDATE RECIPES set RECIPE_NAME = '{rname}', INGREDIENTS = '{ingredients}', INSTRUCTIONS = '{instructions}' WHERE ID = {row[0]}")
                    conn.commit()
                    input("\nRecipe updated! (press enter to continue)")
                elif choice == 4:
                    d = input("\nAre you sure you want to delete this recipe? (\"y\" to confirm)\n> ")
                    if d.lower() == "y":
                        conn.execute(f"DELETE from RECIPES WHERE ID = {row[0]}")
                        conn.commit()
                        input("\nRecipe deleted. (press enter to continue)")
                    else:
                        input("\nRecipe not deleted. (press enter to continue)")

    print("\nBon appetit!\n")

if __name__ == "__main__":
    main()