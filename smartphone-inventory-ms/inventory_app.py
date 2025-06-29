from phone import Phone
import json
from pathlib import Path

#how do i implement my inventory?
DATA_FILE = Path("phone_inventory.json")

def load_inventory():
    with DATA_FILE.open("r") as f:
        data = json.load(f)            
        return [Phone.from_dict(item) for item in data]


def save_inventory(phone_inventory):
       with DATA_FILE.open("w") as f:
           json.dump([phone.to_dict() for phone in phone_inventory], f, indent = 4)
        
# add a phone in inventory
# ask the phone details from user before adding the phone to inventory
#TODO need to handle exceptions
#TODO how to prevent duplicate phone model numbers??
def add_phone(phone_inventory):
    model = input("Enter the phone model: ").strip()
    brand = input("Enter the phone brand: ").strip()
    price = int(input("Enter the phone price: "))
    storage = input("Enter the phone storage: ").strip()
    quantity = int(input("Enter the phone quantity: "))

    phone = Phone(model,brand, price, storage, quantity)

    phone_inventory.append(phone)

    print(f"{model} added succesfully!!")
    save_inventory(phone_inventory)


# view details of a phone
#TODO how do i show information of the phone that the user wants?
def view_phone_details(phone_inventory):
    i = 1
    print("| S.N | Phone Model   |  Brand  |  Storage  |  Price  |  Quantity  |")
    for phone in phone_inventory:
        print("-----------------------------------------------------------------")
        print(f"| {i} | {phone.get_model()} | {phone.get_brand()} | {phone.get_storage()} | {phone.get_price()} | {phone.get_quantity()}  |")
        i = i+1
        
        
# update detail of phones
def update_phone_details(phone_inventory):
    model_number_to_update = input("Enter the phone model number to update: ").strip()
    for phone in phone_inventory:
        if model_number_to_update == phone.get_model():
            new_model_number = input("Enter model number:")
            new_brand = input("Enter brand: ")
            phone.set_model(new_model_number)
            phone.set_brand(new_brand)
            print(f"{model_number_to_update} has been updated\n")
            save_inventory(phone_inventory)
            return
    print(f"{model_number_to_update} not found in records\n")
             
# delete a phone
def delete_phone(phone_inventory):
    model_number_to_delete = input("Enter the phone model to delete: ")
    for phone in phone_inventory:
        if model_number_to_delete == phone.get_model():
            phone_inventory.remove(phone)
            print(f"{model_number_to_delete} has been removed from the records....\n")
            save_inventory(phone_inventory)  
            return
    print(f"{model_number_to_delete} not found in the records....\n")
    
# how to allow users to do the operations?
# how to let the user use the program as much as they want?
# how to let the user exit the program?
def menu():
    phone_inventory = load_inventory()
    while(True):
        print("Enter 1 to add phone: ")
        print("Enter 2 to view phone detail: ")
        print("Enter 3 to update phone detail: ")
        print("Enter 4 to remove a phone: ")
        print("Enter 5 to exit: ")
        try:
            option = int(input("Choose an option: "))
            if(option == 1):
                add_phone(phone_inventory)
            elif(option == 2):
                view_phone_details(phone_inventory)
            elif(option == 3):
                update_phone_details(phone_inventory)
            elif(option == 4):
                delete_phone(phone_inventory)
            elif(option == 5):
                print("Thank you, See You Again!!")
                break
            else:
                print("Enter the options from (1 to 5)\n")
        except ValueError:
            print("Invalid entry!!! Enter from 1 to 5...")
        # except:
        #     print("Cannot perform the action!!!")

if __name__ == '__main__':
# to execute the file only when used
# when a module is imported in another module, 
# then the Python interpreter will assign the string with 
# the name of that module to the special variable __name__
    menu()