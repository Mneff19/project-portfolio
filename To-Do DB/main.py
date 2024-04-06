import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import re

API_KEY = 'AIzaSyCCkneJqCbQtZrDu3jYi7dJyfybkHI1Xz8'
SIGNUP_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}'
SIGNIN_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}'

# Connect to Firestore
cred = credentials.Certificate('./serviceCreds.json') # Use a service account.
app = firebase_admin.initialize_app(cred) # connect to firebase
db = firestore.client() # connect to firestore
    
# Loop until an integer choice within the provided range is provided
def get_int_input_within_range(max, min = 1):
    choice = min - 1

    # Loop until valid choice provided
    while choice == min - 1:
        resp = input("> ")

        if resp.isnumeric():
            # If user gave number, convert to int
            resp = int(resp)
            # If falls within valid response range
            if resp > min - 1 and resp < max + 1:
                choice = resp
            else:
                # Display error message
                print(f"Please enter a number 1-{max}")
        else:
            # Display error message
            print(f"Please enter a number 1-{max}")

    return choice

# Get validated email from the user
def get_valid_email():
    email_validate_pattern = r"^\S+@\S+\.\S+$"
    email = None

    while email is None:
        rawEmail = input("Email: ")
        if (re.match(email_validate_pattern, rawEmail)):
            email = rawEmail
        else:
            print("Please enter a valid email.")
    return email

# Handle user sign up
def handle_sign_up():
    user_token = None
    signup_headers = {'content-type': 'application/json'}

    while user_token is None:
        email = get_valid_email()
        password = input("Password: ")

        signup_payload = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        r = requests.post(SIGNUP_URL, signup_payload, signup_headers)
        rJson = r.json()
        if ('error' in rJson):
            # Sample output:
            # {'error': {'code': 400, 'message': 'EMAIL_EXISTS', 'errors': [{'message': 'EMAIL_EXISTS', 'domain': 'global', 'reason': 'invalid'}]}}
            print("ERROR: Email already exists. Please try again.\n")
        else:
            # Sample output:
            # {'kind': 'identitytoolkit#SignupNewUserResponse', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6IkJrbmtldjQyWm9NMGVwdU1LeTJVd3BJN1ZnQzIiLCJzdWIiOiJCa25rZXY0MlpvTTBlcHVNS3kyVXdwSTdWZ0MyIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTkrdGVzdHRoYXRkYjJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5K3Rlc3R0aGF0ZGIyQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.JCKjax0pzhWSdTkmEs-v2f_YWrtblCwkBER21gUCsdUrrjYxAJ_3FyU29mttAWerqHXkhdexNQqE3xeisMR9vbKKX_yP6L1PamwyGdao-vtgJciuU5WaoNV29XxAoQYJin4K_GtUL6Be8P8eGd1dUJyecoHAm19-CPa2oyE-xAwslH_vvOQTa-XS2t7_ovG4JmbwEVtGEVhGz08C4MClWFwLkbLiMPa2oKGyKE-WSL01eZAWnNHcSsYbyKTzNSHR6wm86eSxTthy9D5JoLgCmOJyK1EGC3ETvhEdLenmxr3eo6Wjf_x9aqxrG7Ee4MBCAiL8FlEnpA8TargXr-rtdw', 'email': 'mpneff19+testthatdb2@gmail.com', 'refreshToken': 'AMf-vBy1W1sOHwkQXjYNp9rDA3zVdF4wot4M1y5WrEEQs97JSJGY-QNbOmX7XCSll21sACziirgmaJa0RaSoRf8i8_ZtIixkRx84vSf2rb2YwgGFQekiouwAzfgmehMkO-LBwI_K7CveVYwufM-cixpRsy6sdSlBrBLUJDIYxAj8Rdiv16u7zUqcDoH9Yk1nB-NdS1T-BFaf74L4cRuXJab0jZ8ZNXqpGzdQWGPeMQXNlvGQLKIOPcM', 'expiresIn': '3600', 'localId': 'Bknkev42ZoM0epuMKy2UwpI7VgC2'}
            print("Account created successfully!\n")
            user_token = rJson['localId']
    return user_token

# Handle user sign in
def handle_sign_in():
    user_token = None
    signin_headers = {'content-type': 'application/json'}

    while user_token is None:
        email = get_valid_email()
        password = input("Password: ")

        signin_payload = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        r2 = requests.post(SIGNIN_URL, signin_payload, signin_headers)
        r2Json = r2.json()
        if ('error' in r2Json):
            # Sample output:
            # {'error': {'code': 400, 'message': 'INVALID_LOGIN_CREDENTIALS', 'errors': [{'message': 'INVALID_LOGIN_CREDENTIALS', 'domain': 'global', 'reason': 'invalid'}]}}
            print("ERROR: Invalid email or password. Please try again.")
        else:
            # Sample output:
            # {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': '9wF2J9Mb1XROHJk0u2H4LD4o5Uj1', 'email': 'mpneff19@gmail.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6Ijl3RjJKOU1iMVhST0hKazB1Mkg0TEQ0bzVVajEiLCJzdWIiOiI5d0YySjlNYjFYUk9ISmswdTJINExENG81VWoxIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.gejE0ts69BX_5omnj9uv-2Gu3ULG38hjRxQxblCeFVQnAgkaddFNnIYxhIEDrxO0ooGj_VBer9koeCl-KaUM_0HQr27yWL4aZmR-1vS9ii9IQZ6S7X2ll-F9fGgNoLdKdgN9ezBuUkWGqF4TwNqYfY8xJG6znkyqanb2v7HLbjiWteyUYCu1bxGJJFYK6jr9_ediqo9lcyL25-synGvOGiivdxJlbSsVlIVJF0cQFz2rJmOkatpV1eyar5Akz8Imw4Y9A9sN8fk-_vGuomFwP76wi9KJXTv8ACQlQsHX1LKFpmkcBiRvc9yGSSLAexRwa0qmUpJo6HK_3ENvonAuNg', 'registered': True, 'refreshToken': 'AMf-vBxsJcoXg9LCUV2-KXg2Tpy7Wb4RGIU6PW1kPIN5f6TI9hzIempWsxHQnZp-cPkH10gOaY6q0YcXOxDmOnvipAzZzNN2UwQ1UXOSjdYGe53GCT5md8Bo4QZ4qde4Ar4gEd5KnB3g47J5HpolrXeCfIMo1KxzkMWCdTZPNvukYVXcbz3J5YpsmApTpMsLmsqziskT53QW71aiSsLNfB3Gb9jrSaiDUg', 'expiresIn': '3600'}
            user_token = r2Json['localId']
            print("Signed in successfully!\n\n")
    return user_token

# Displays authentication menu options
def display_authentication_menu():
   print("\n\nPlease select an option:")
   print(" 1) Sign In")
   print(" 2) Sign Up")
   print(" 3) Quit") 

# Handles user auth
def authenticate_user():
    user_token = None
    auth_choice = 0 # While loop condition
    # Run program until exit code (3) is given
    while user_token is None and auth_choice < 3:
        # Show menu
        display_authentication_menu()
        # Get valid input
        auth_choice = get_int_input_within_range(3)

        # Handle sign in and sign up choices
        if auth_choice == 1:
            user_token = handle_sign_in()
        elif auth_choice == 2:
            user_token = handle_sign_up()
    return user_token

# Displays empty options (no current or past todo items)
def display_main_options_empty():
    print("What would you like to do?")
    print(" 1) Add Item")
    print(" 2) Quit")

# Displays limited options (only past items, no current)
def display_main_options_limited():
    print("What would you like to do?")
    print(" 1) Add Item")
    print(" 2) See completed items")
    print(" 3) Quit")
    
# Displays all main options for user to take (current and past todo items)
def display_main_options_full():
    print("What would you like to do?")
    print(" 1) Add Item")
    print(" 2) Edit Item")
    print(" 3) Mark Item Complete")
    print(" 4) See completed items")
    print(" 5) Quit")

# Displays user's todo items
def display_user_todo_items(current_doc_list):
    if(len(current_doc_list) > 0):
        print("Here are your current To-Do items:")
        for doc in current_doc_list:
            doc_info = doc.get().to_dict()
            if not doc_info['completed']:
                print(f"  ☐ {['title']}")
    else:
        print("There are no current items in your list.")

# Runs To Do App for specified user
def run_todo_app_for_user(user_token):
    user_doc_ref = db.collection("todoitems").document(user_token)
    print("Welcome to your To-Do DB!\n")

    todo_choice = 0
    todo_choice_max = 5
    while todo_choice < todo_choice_max:
        todo_choice = 0
        doc_list = user_doc_ref.collection("todos").list_documents()
        current_doc_list = list(filter(lambda doc:doc.get().to_dict()['completed'] == True, doc_list))

        display_user_todo_items(current_doc_list)
        print() # new line
        if len(current_doc_list) > 0:
            display_main_options_full()
            todo_choice_max = 5
        elif len(list(doc_list)) > 0:
            display_main_options_limited()
            todo_choice_max = 3
        else:
            display_main_options_empty()
            todo_choice_max = 2
        todo_choice = get_int_input_within_range(todo_choice_max)

def worskhop():
    # signup_payload = {
    #     'email': 'mpneff19+testthatdb2@gmail.com',
    #     'password': 'test123',
    #     'returnSecureToken': True
    # }
    # signup_headers = {'content-type': 'application/json'}
    # r = requests.post(SIGNUP_URL, signup_payload, signup_headers)
    # rJson = r.json()
    # if ('error' in rJson):
    #     print(rJson)
    #     print("email already exists dummyyyy")
    #     # Sample output:
    #     # {'error': {'code': 400, 'message': 'EMAIL_EXISTS', 'errors': [{'message': 'EMAIL_EXISTS', 'domain': 'global', 'reason': 'invalid'}]}}
    # else:
    #     print(rJson)
    #     print("Account created successfully!")
    #     # Sample output:
    #     # {'kind': 'identitytoolkit#SignupNewUserResponse', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6IkJrbmtldjQyWm9NMGVwdU1LeTJVd3BJN1ZnQzIiLCJzdWIiOiJCa25rZXY0MlpvTTBlcHVNS3kyVXdwSTdWZ0MyIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTkrdGVzdHRoYXRkYjJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5K3Rlc3R0aGF0ZGIyQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.JCKjax0pzhWSdTkmEs-v2f_YWrtblCwkBER21gUCsdUrrjYxAJ_3FyU29mttAWerqHXkhdexNQqE3xeisMR9vbKKX_yP6L1PamwyGdao-vtgJciuU5WaoNV29XxAoQYJin4K_GtUL6Be8P8eGd1dUJyecoHAm19-CPa2oyE-xAwslH_vvOQTa-XS2t7_ovG4JmbwEVtGEVhGz08C4MClWFwLkbLiMPa2oKGyKE-WSL01eZAWnNHcSsYbyKTzNSHR6wm86eSxTthy9D5JoLgCmOJyK1EGC3ETvhEdLenmxr3eo6Wjf_x9aqxrG7Ee4MBCAiL8FlEnpA8TargXr-rtdw', 'email': 'mpneff19+testthatdb2@gmail.com', 'refreshToken': 'AMf-vBy1W1sOHwkQXjYNp9rDA3zVdF4wot4M1y5WrEEQs97JSJGY-QNbOmX7XCSll21sACziirgmaJa0RaSoRf8i8_ZtIixkRx84vSf2rb2YwgGFQekiouwAzfgmehMkO-LBwI_K7CveVYwufM-cixpRsy6sdSlBrBLUJDIYxAj8Rdiv16u7zUqcDoH9Yk1nB-NdS1T-BFaf74L4cRuXJab0jZ8ZNXqpGzdQWGPeMQXNlvGQLKIOPcM', 'expiresIn': '3600', 'localId': 'Bknkev42ZoM0epuMKy2UwpI7VgC2'}

    # print("anywayyyyy")

    userId = None
    signin_payload = {
        'email': 'mpneff19+testthatdb2@gmail.com',
        'password': 'test123',
        'returnSecureToken': True
    }
    signin_headers = {'content-type': 'application/json'}
    r2 = requests.post(SIGNIN_URL, signin_payload, signin_headers)
    r2Json = r2.json()
    if ('error' in r2Json):
        print(r2Json)
        print("email doesn't exist silly")
        # Sample output:
        # {'error': {'code': 400, 'message': 'INVALID_LOGIN_CREDENTIALS', 'errors': [{'message': 'INVALID_LOGIN_CREDENTIALS', 'domain': 'global', 'reason': 'invalid'}]}}
    else:
        print(r2Json)
        userId = r2Json['localId']
        print("Signed in successfully!")
        # Sample output:
        # {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': '9wF2J9Mb1XROHJk0u2H4LD4o5Uj1', 'email': 'mpneff19@gmail.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6Ijl3RjJKOU1iMVhST0hKazB1Mkg0TEQ0bzVVajEiLCJzdWIiOiI5d0YySjlNYjFYUk9ISmswdTJINExENG81VWoxIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.gejE0ts69BX_5omnj9uv-2Gu3ULG38hjRxQxblCeFVQnAgkaddFNnIYxhIEDrxO0ooGj_VBer9koeCl-KaUM_0HQr27yWL4aZmR-1vS9ii9IQZ6S7X2ll-F9fGgNoLdKdgN9ezBuUkWGqF4TwNqYfY8xJG6znkyqanb2v7HLbjiWteyUYCu1bxGJJFYK6jr9_ediqo9lcyL25-synGvOGiivdxJlbSsVlIVJF0cQFz2rJmOkatpV1eyar5Akz8Imw4Y9A9sN8fk-_vGuomFwP76wi9KJXTv8ACQlQsHX1LKFpmkcBiRvc9yGSSLAexRwa0qmUpJo6HK_3ENvonAuNg', 'registered': True, 'refreshToken': 'AMf-vBxsJcoXg9LCUV2-KXg2Tpy7Wb4RGIU6PW1kPIN5f6TI9hzIempWsxHQnZp-cPkH10gOaY6q0YcXOxDmOnvipAzZzNN2UwQ1UXOSjdYGe53GCT5md8Bo4QZ4qde4Ar4gEd5KnB3g47J5HpolrXeCfIMo1KxzkMWCdTZPNvukYVXcbz3J5YpsmApTpMsLmsqziskT53QW71aiSsLNfB3Gb9jrSaiDUg', 'expiresIn': '3600'}


    doc_ref = db.collection("todoitems").document(userId)
    iterate_ref = doc_ref.collection("todos").list_documents()
    item_ref = doc_ref.collection("todos").document()
    item_ref.set({"title": "test item", "completed": False})
    # update_data = {"duedate": firestore.DELETE_FIELD}
    update_data = {"completed": True}

    i = 0
    for doc in iterate_ref:
        if i == 4:
            doc.update(update_data)
        print(f"{doc.id} => {doc.get().to_dict()}")
        if i == 2:
            doc.delete()
            i += 1
            print(f"<!-- {doc.id} DELETED --!>")
        i += 1

    # doc_ref = db.collection("users").document("aturing")
    # doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})
    
    auth_choice = 0 # While loop condition
    # Run program until exit code (3) is given
    while auth_choice < 3:
        # Reset auth_choice and show menu
        auth_choice = 0
        display_authentication_menu()

        # Loop until valid input is given
        while auth_choice == 0:
            auth_resp = input("> ")

            if auth_resp.isnumeric():
                # If user gave number, convert to int
                auth_resp = int(auth_resp)
                # If falls within valid auth_response range
                if auth_resp > 0 and auth_resp < 3:
                    auth_choice = auth_resp
                else:
                    # Display error message
                    print("Please enter a number 1-2")
            else:
                # Display error message
                print("Please enter a number 1-2")
        
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



# The main program
def main():
    print("\nWelcome to To-Do DB!") # Displays welcome message outside of loop

    # Authentication, will return false if user decides to exit
    user_token = authenticate_user()
    if not user_token:
        return
    
    # Run To-Do DB App for the given user
    run_todo_app_for_user(user_token)

# Run main
if __name__ == "__main__":
    main()