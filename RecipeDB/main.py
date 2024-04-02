import sqlite3

# Displays main menu
def show_menu():
   print("\n\nPlease select an option:")
   print(" 1) See Recipes")
   print(" 2) Add Recipe")
   print(" 3) Edit Recipe")
   print(" 4) Delete Recipe")
   print(" 5) Quit")

# Prompts the user for items until the terminator is provided,
# assembling the responses into a specifically formatted string
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

# The main program
def main():
    # Connect to the DB
    conn = sqlite3.connect('test.db')
    choice = 0 # While loop condition

    # Create the table if it doesn't already exist
    conn.execute('''CREATE TABLE IF NOT EXISTS RECIPES
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                RECIPE_NAME      TEXT   NOT NULL,
                INGREDIENTS      TEXT   NOT NULL,
                INSTRUCTIONS     TEXT   NOT NULL);''')

    print("\nWelcome to RecipeDB!") # Displays welcome message outside of loop
    # Run program until exit code (5) is given
    while choice < 5:
        # Reset choice and show menu
        choice = 0
        show_menu()

        # Loop until valid input is given
        while choice == 0:
            resp = input("> ")

            if resp.isnumeric():
                # If user gave number, convert to int
                resp = int(resp)
                # If falls within valid response range
                if resp > 0 and resp < 6:
                    choice = resp
                else:
                    # Display error message
                    print("Please enter a number 1-5")
            else:
                # Display error message
                print("Please enter a number 1-5")
        
        if choice == 2:
            # Adding recipe, so get name, ingredient list, and instructions
            rname = input("\nWhat is the name of the recipe?\n> ")
            ingredients = get_input_list_str_with_prompt("\nWhat are the ingredients? (add one at a time,  hit enter to stop)")
            instructions = get_input_list_str_with_prompt("\nWhat are the instructions? (add one at a time,  hit enter to stop)")

            # Run SQL query with provided variables
            conn.execute(f"INSERT INTO RECIPES (RECIPE_NAME,INGREDIENTS,INSTRUCTIONS) \
                  VALUES ('{rname}', '{ingredients}', '{instructions}' )")
            conn.commit() # Save changes in DB
            input("Recipe added! (press enter to continue)") # Wait for user input to proceed
        elif choice < 5:
            # View, edit, or delete recipe options
            print() # New line for formatting
            # Displays list of recipes
            recipe_cursor = conn.execute("SELECT id, recipe_name, ingredients, instructions from RECIPES") # Gets all recipes
            recipe_rows = recipe_cursor.fetchall() # Convert SQL cursor to array
            if len(recipe_rows) > 0:
                # Show all recipe names with ID, if any recipes are in the DB
                for row in recipe_rows:
                    print(f"{row[0]}) {row[1]}")
                # Show recipe selection text
                print("\nEnter the ID of the recipe you wish to select, or 0 to exit")

                chosen_id = -1 # While loop condition, also used after loop
                while chosen_id < 0:
                    # Loop until valid recipe ID is provided or exit code given
                    new_id = input("> ")
                    if new_id.isnumeric():
                        # If user gave number, convert to int
                        new_id = int(new_id)
                        if new_id == 0:
                            # Exit code, breaks loop
                            chosen_id = new_id
                        else:
                            # Try to grab recipe with given ID
                            selected_cursor = conn.execute(f'''SELECT ID FROM RECIPES WHERE ID={new_id};''')
                            if len(selected_cursor.fetchall()) > 0:
                                # ID was found! Set loop condition and break loop
                                chosen_id = new_id
                            else:
                                # No recipe found with ID
                                print("Please enter a valid ID")
                    else:
                        # Invalid ID string given
                        print("Please enter a valid ID")
            else:
                # No recipes in DB
                input("No recipes to show. Press enter to contiue.") # Wait for user input to proceed

            # Grab chosen recipe from DB
            chosen_recipe = conn.execute(f'''SELECT ID, RECIPE_NAME, INGREDIENTS, INSTRUCTIONS FROM RECIPES WHERE ID={chosen_id};''')
            for row in chosen_recipe:
                # Show recipe detail view!
                print(f"\n{row[1]}")
                print("\nIngredients:")
                for ingredient in row[2].split(",,,"):
                    print(f"- {ingredient}")
                print("\nInstructions:")
                for instruction in row[3].split(",,,"):
                    print(f"- {instruction}")

                if choice == 1:
                    # Show recipe, all done!
                    input("\nPress enter to exit.") # Wait for user input to proceed
                elif choice == 3:
                    # Edit recipe, set values to what's currently in DB
                    rname = row[1]
                    ingredients = row[2]
                    instructions = row[3]

                    edit_choice = 0 # While loop condition
                    while edit_choice < 4:
                        edit_choice = 0 # Reset choice
                        # Allow user to pick what they'd like to edit
                        print("Select the following to edit:")
                        print(" 1) Recipe Name")
                        print(" 2) Ingredients")
                        print(" 3) Instructions")
                        print(" 4) Exit")

                        while edit_choice == 0:
                            # Loop until user provides valid input
                            e_choice = input("> ")

                            if e_choice.isnumeric():
                                # If user gave number, convert to int
                                e_choice = int(e_choice)
                                if e_choice > 0 and e_choice < 5:
                                    # Valid choice provided! Break loop
                                    edit_choice = e_choice
                                else:
                                    # Int given, but not in range
                                    print("Please enter a number 1-4")
                            else:
                                # Invalid string given
                                print("Please enter a number 1-4")

                        if edit_choice == 1:
                            # Get new recipe name and override stored value
                            rname = input("\nWhat would you like the new name of the recipe to be?\n> ")
                        elif edit_choice == 2:
                            # Get new ingredients and override stored value
                            ingredients = get_input_list_str_with_prompt("\nWhat is the new list of ingredients? (add one at a time, hit enter to stop)")
                        elif edit_choice == 3:
                            # Get new instructions and override stored value
                            instructions = get_input_list_str_with_prompt("\nWhat is the new set of instructions? (add one at a time, hit enter to stop)")
                        
                    # Update values in DB - this will preserve the values even if the user did not choose to edit them
                    conn.execute(f"UPDATE RECIPES set RECIPE_NAME = '{rname}', INGREDIENTS = '{ingredients}', INSTRUCTIONS = '{instructions}' WHERE ID = {row[0]}")
                    conn.commit() # Save in DV
                    input("\nRecipe updated! (press enter to continue)") # Wait for user input to proceed
                elif choice == 4:
                    # Delete recipe
                    d = input("\nAre you sure you want to delete this recipe? (\"y\" to confirm)\n> ") # Confirm with user
                    if d.lower() == "y":
                        # Yes, delete recipe
                        conn.execute(f"DELETE from RECIPES WHERE ID = {row[0]}") # Perform SQL
                        conn.commit() # Save in DB
                        input("\nRecipe deleted. (press enter to continue)") # Wait for user input to proceed
                    else:
                        # User cancelled delete request, back out
                        input("\nRecipe not deleted. (press enter to continue)") # Wait for user input to proceed

    # User exited main loop, display goodbye message
    print("\nBon appetit!\n")

# Run main
if __name__ == "__main__":
    main()