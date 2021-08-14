import os
import pymongo
if os.path.exists("env.py"):
    import env

# Set Constant Variables
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"

# function to connect to DB
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("") # Empty str to leave a blank line at the top of our menu each time
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")  #menu options giving CRUD fucntionaility

    option = input("Enter option: ")  # Creates a variable for user input
    return option  # Returns what the user had selected

# Helper Function. First and last are asking the user to input details to find
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last Name > ")
# try/except block
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
        # doc = coll.find_one({"last": last.lower()})  # Doc is a cursor object.
        # If search find someone, it will be stored in the Mongo Cursor object
    except:
        print("Error accessing the db")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")
# Creating a new var, dictionary, using variale names from above as the values that will be injected into the DB
# KEYS:VALUE
# Dictionary to insert into the DB
    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert(new_doc) # trying to insert the new dict into the collectiona variable defined globally
        print("")
        print("Document Inserted")
    except:
        print("Error accessing DB") # In real world, drill down more to cath specific errors


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
                
        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("document updated")
        except:
            print("Error accessing the DB")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted")
            except:
                print("error accessing the DB")
        else:
            print("doc not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("You have selected an invalid option") # to handle anything else the user might have input
        print("") # After menu displayed, blank line for visual


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()