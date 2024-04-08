import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import re

# Constants for use in communicating with the cloud
API_KEY = 'AIzaSyCCkneJqCbQtZrDu3jYi7dJyfybkHI1Xz8'
SIGNUP_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}'
SIGNIN_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}'
HEADERS = {'content-type': 'application/json'}

# Connect to Firestore
cred = credentials.Certificate('./serviceCreds.json') # Use a service account.
app = firebase_admin.initialize_app(cred) # connect to firebase
db = firestore.client() # connect to firestore
    
# Loop until an integer choice within the provided range is provided
def get_int_input_within_range(max, min = 1):
    choice = min - 1 # Initiate while loop condition

    # Loop until valid choice provided
    while choice == min - 1:
        resp = input("> ") # Get raw input

        if resp.isnumeric():
            # If user gave number, convert to int
            resp = int(resp)
            # If falls within valid response range
            if resp > min - 1 and resp < max + 1:
                choice = resp # Override while condition to break the loop
            else:
                print(f"Please enter a number 1-{max}") # Display error message
        else:
            print(f"Please enter a number 1-{max}") # Display error message

    return choice

# Get validated email from the user
def get_valid_email():
    email_validate_pattern = r"^\S+@\S+\.\S+$" # Regex pattern to confirm email format
    email = None # Initalize while loop condition

    # Loop until valid email is provided
    while email is None:
        rawEmail = input("Email: ") # Raw user input
        # Check format with Regex
        if (re.match(email_validate_pattern, rawEmail)):
            email = rawEmail
        else:
            print("Please enter a valid email.") # Display error message
    return email

# Handle user sign up
def handle_sign_up():
    user_token = None # Initalize while loop condition 

    # Loop until user successfully signs up
    while user_token is None:
        email = get_valid_email() # Loops until valid email provided
        password = input("Password: ") # Any password is acceptable

        # Construct payload
        signup_payload = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        r = requests.post(SIGNUP_URL, signup_payload, HEADERS) # Send request
        rJson = r.json() # Interpret response
        # If error, display message and keep looping
        if ('error' in rJson):
            # Sample output:
            # {'error': {'code': 400, 'message': 'EMAIL_EXISTS', 'errors': [{'message': 'EMAIL_EXISTS', 'domain': 'global', 'reason': 'invalid'}]}}
            print("ERROR: Email already exists. Please try again.\n")
        else:
            # Sample output:
            # {'kind': 'identitytoolkit#SignupNewUserResponse', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6IkJrbmtldjQyWm9NMGVwdU1LeTJVd3BJN1ZnQzIiLCJzdWIiOiJCa25rZXY0MlpvTTBlcHVNS3kyVXdwSTdWZ0MyIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTkrdGVzdHRoYXRkYjJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5K3Rlc3R0aGF0ZGIyQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.JCKjax0pzhWSdTkmEs-v2f_YWrtblCwkBER21gUCsdUrrjYxAJ_3FyU29mttAWerqHXkhdexNQqE3xeisMR9vbKKX_yP6L1PamwyGdao-vtgJciuU5WaoNV29XxAoQYJin4K_GtUL6Be8P8eGd1dUJyecoHAm19-CPa2oyE-xAwslH_vvOQTa-XS2t7_ovG4JmbwEVtGEVhGz08C4MClWFwLkbLiMPa2oKGyKE-WSL01eZAWnNHcSsYbyKTzNSHR6wm86eSxTthy9D5JoLgCmOJyK1EGC3ETvhEdLenmxr3eo6Wjf_x9aqxrG7Ee4MBCAiL8FlEnpA8TargXr-rtdw', 'email': 'mpneff19+testthatdb2@gmail.com', 'refreshToken': 'AMf-vBy1W1sOHwkQXjYNp9rDA3zVdF4wot4M1y5WrEEQs97JSJGY-QNbOmX7XCSll21sACziirgmaJa0RaSoRf8i8_ZtIixkRx84vSf2rb2YwgGFQekiouwAzfgmehMkO-LBwI_K7CveVYwufM-cixpRsy6sdSlBrBLUJDIYxAj8Rdiv16u7zUqcDoH9Yk1nB-NdS1T-BFaf74L4cRuXJab0jZ8ZNXqpGzdQWGPeMQXNlvGQLKIOPcM', 'expiresIn': '3600', 'localId': 'Bknkev42ZoM0epuMKy2UwpI7VgC2'}
            user_token = rJson['localId'] # Set token from response to break loop
            print("Account created successfully!\n")
    return user_token

# Handle user sign in
def handle_sign_in():
    user_token = None # Initalize while loop condition 

    # Loop until user successfully signs in
    while user_token is None:
        email = get_valid_email() # Loops until valid email provided
        password = input("Password: ") # Any password is acceptable

        # Construct payload
        signin_payload = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        r2 = requests.post(SIGNIN_URL, signin_payload, HEADERS) # Send request
        r2Json = r2.json() # Interpret response
        # If error, display message and keep looping
        if ('error' in r2Json):
            # Sample output:
            # {'error': {'code': 400, 'message': 'INVALID_LOGIN_CREDENTIALS', 'errors': [{'message': 'INVALID_LOGIN_CREDENTIALS', 'domain': 'global', 'reason': 'invalid'}]}}
            print("ERROR: Invalid email or password. Please try again.")
        else:
            # Sample output:
            # {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': '9wF2J9Mb1XROHJk0u2H4LD4o5Uj1', 'email': 'mpneff19@gmail.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6Ijl3RjJKOU1iMVhST0hKazB1Mkg0TEQ0bzVVajEiLCJzdWIiOiI5d0YySjlNYjFYUk9ISmswdTJINExENG81VWoxIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.gejE0ts69BX_5omnj9uv-2Gu3ULG38hjRxQxblCeFVQnAgkaddFNnIYxhIEDrxO0ooGj_VBer9koeCl-KaUM_0HQr27yWL4aZmR-1vS9ii9IQZ6S7X2ll-F9fGgNoLdKdgN9ezBuUkWGqF4TwNqYfY8xJG6znkyqanb2v7HLbjiWteyUYCu1bxGJJFYK6jr9_ediqo9lcyL25-synGvOGiivdxJlbSsVlIVJF0cQFz2rJmOkatpV1eyar5Akz8Imw4Y9A9sN8fk-_vGuomFwP76wi9KJXTv8ACQlQsHX1LKFpmkcBiRvc9yGSSLAexRwa0qmUpJo6HK_3ENvonAuNg', 'registered': True, 'refreshToken': 'AMf-vBxsJcoXg9LCUV2-KXg2Tpy7Wb4RGIU6PW1kPIN5f6TI9hzIempWsxHQnZp-cPkH10gOaY6q0YcXOxDmOnvipAzZzNN2UwQ1UXOSjdYGe53GCT5md8Bo4QZ4qde4Ar4gEd5KnB3g47J5HpolrXeCfIMo1KxzkMWCdTZPNvukYVXcbz3J5YpsmApTpMsLmsqziskT53QW71aiSsLNfB3Gb9jrSaiDUg', 'expiresIn': '3600'}
            user_token = r2Json['localId'] # Set token from response to break loop
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

# Displays empty options (no current, only past todo items)
def display_main_options_no_current():
    print("What would you like to do?")
    print(" 1) Add Item")
    print(" 2) See Completed Items")
    print(" 3) Quit")

# Displays limited options (only current todo items)
def display_main_options_limited():
    print("What would you like to do?")
    print(" 1) Add Item")
    print(" 2) Edit Item")
    print(" 3) Mark Item Complete")
    print(" 4) Quit")
    
# Displays all main options for user to take (current and past todo items)
def display_main_options_full():
    print("What would you like to do?")
    print(" 1) Add Item")
    print(" 2) Edit Item")
    print(" 3) Mark Item Complete")
    print(" 4) See Completed Items")
    print(" 5) Quit")

# Displays user's todo items
def display_user_todo_items(current_doc_list):
    print() # New line for formatting
    # If items to show
    if(len(current_doc_list) > 0):
        # Show each item in their to do list
        print("Your To-Do Items:")
        for doc in current_doc_list:
            doc_info = doc.get().to_dict() # Store actual item data
            print(f"  ☐ {doc_info['title']}")
    else:
        print("There are no current items in your list.")
        
# Sets up menu displaying a numbered list of todo items, returning an array of the ids of each item
def setup_numbered_todo_list(current_doc_list):
    ids = [] # Initialize return array
    i_item = 1 # For displaying number next to each item

    # Show each completed item
    for doc in current_doc_list:
        doc_info = doc.get().to_dict() # Store actual item data
        print(f"  {i_item}) {doc_info['title']}")
        # Add item ID to the return array
        ids.append(doc.id)
        i_item +=  1 # increment tracker
    return ids

# Adds todo item to the user's collection
def add_todo_item(user_doc_ref):
    # Get title from user
    todo_title = input("\nWhat do you need to do?\n> ")
    # Access user's todo collection
    item_ref = user_doc_ref.collection("todos").document()
    # Add item
    item_ref.set({"title": todo_title, "completed": False})
    print("Item added!")

# Edits todo item from the user's collection
def edit_todo_item(user_doc_ref, current_doc_list):
    print("\nPlease select an item to edit:")
    # Display each item and get array of their IDs
    id_list = setup_numbered_todo_list(current_doc_list)
    # Get user's choice
    id_choice = get_int_input_within_range(len(id_list)) - 1
    # Get updated title from user
    updated_title = input("\nWhat would you like to change this task to say?\n> ")
    # Get the specified item in the database
    item_ref = user_doc_ref.collection("todos").document(id_list[id_choice])
    # Update item
    item_ref.update({"title": updated_title})
    print("Item updated!")

# Complete todo item from the user's collection
def complete_todo_item(user_doc_ref, current_doc_list):
    print("\nPlease select an item to complete:")
    # Display each item and get array of their IDs
    id_list = setup_numbered_todo_list(current_doc_list)
    # Get user's choice
    id_choice = get_int_input_within_range(len(id_list)) - 1
    # Get the specified item in the database
    item_ref = user_doc_ref.collection("todos").document(id_list[id_choice])
    # Update item
    item_ref.update({"completed": True})
    print("Item completed!")

# Show completed todo items, allowing user to delete one if wanted
def handle_completed_todo_items(user_doc_ref, completed_doc_list):
    print("\nCompleted Items:")
    # Display each item and get array of their IDs
    id_list = setup_numbered_todo_list(completed_doc_list)
    # Get user's choice of deleting or not
    is_deleting = True if input("Delete an item? (y/N) ").lower() == "y" else False
    if is_deleting:
        print("Which item will you delete?")
        # Get user's choice
        id_choice = get_int_input_within_range(len(id_list)) - 1
        # Get the specified item in the database
        item_ref = user_doc_ref.collection("todos").document(id_list[id_choice])
        # Delete
        item_ref.delete()
        print("Item deleted!")

# Gets the menu option dictionary based on the number of menu items
def get_menu_option_dict(num_menu_items):
    # Construct and return menu options based on number of options in menu
    # Not an ideal solution, could easily be iterated on and improved
    if num_menu_items == 2:
        return {"add": 1}
    if num_menu_items == 3:
        return {"add": 1, "show_completed": 2}
    if num_menu_items == 4:
        return {"add": 1, "edit": 2, "complete": 3}
    if num_menu_items == 5:
        return {"add": 1, "edit": 2, "complete": 3, "show_completed": 4}

# Runs To Do App for specified user
def run_todo_app_for_user(user_token):
    # Get user's wrapper container
    user_doc_ref = db.collection("todoitems").document(user_token)
    # Show welcome message
    print("Welcome to your To-Do DB!\nPlease wait while your list is fetched...\n")

    # Initialize while loop conditions
    todo_choice = 0
    todo_choice_max = 5
    while todo_choice < todo_choice_max:
        todo_choice = 0 # Reset choice
        # Get updated list of todo items to reflect any changes made during the loop
        doc_list = user_doc_ref.collection("todos")
        # Manipulate doc_list to get necessary sets of information
        current_doc_list = list(filter(lambda doc:doc.get().to_dict()['completed'] == False, doc_list.list_documents())) # To do items not completed
        completed_doc_list = list(filter(lambda doc:doc.get().to_dict()['completed'] == True, doc_list.list_documents())) # To do items completed
        item_count = doc_list.count().get()[0][0].value # Total number of items

        # Show all incomplete todo items (if any)
        display_user_todo_items(current_doc_list)
        print() # new line for formatting
        # Display menu options based on what information the user has in the database
        if item_count == 0:
            # No items, incomplete or complete
            display_main_options_empty()
            todo_choice_max = 2
        elif len(current_doc_list) == 0:
            # No incomplete items, only complete
            display_main_options_no_current()
            todo_choice_max = 3
        elif item_count == len(current_doc_list):
            # No complete items, only incomplete
            display_main_options_limited()
            todo_choice_max = 4
        else:
            # Complete and incomplete items
            display_main_options_full()
            todo_choice_max = 5
        # Get menu options dictionary to convert user input to corresponding menu option
        menu_option_dict = get_menu_option_dict(todo_choice_max)
        # Get user's choice
        todo_choice = get_int_input_within_range(todo_choice_max)

        # If user did not pass the quit integer
        if todo_choice < todo_choice_max:
            # Run corresponding action
            if todo_choice == menu_option_dict['add']:
                # Add item
                add_todo_item(user_doc_ref)
            if 'edit' in menu_option_dict and todo_choice == menu_option_dict['edit']:
                # Edit item
                edit_todo_item(user_doc_ref, current_doc_list)
            if 'complete' in menu_option_dict and todo_choice == menu_option_dict['complete']:
                # Mark item as complete
                complete_todo_item(user_doc_ref, current_doc_list)
            if 'show_completed' in menu_option_dict and todo_choice == menu_option_dict['show_completed']:
                # Show completed items, delete one if wanted
                handle_completed_todo_items(user_doc_ref, completed_doc_list)

# The main program
def main():
    print("\nWelcome to To-Do DB!") # Displays welcome message outside of loop

    # Authentication, will return false if user decides to exit
    user_token = authenticate_user()
    if not user_token:
        return
    
    # Run To-Do DB App for the given user
    run_todo_app_for_user(user_token)

    # Show exit message
    print("\nCome again soon!")

# Run main
if __name__ == "__main__":
    main()