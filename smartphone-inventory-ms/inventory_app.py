from phone import Phone

#how do i implement my inventory?
phone_inventory = [Phone("model","brand",223, "storage", 23),
                   Phone("test1","testbrand1",22223, "teststorage1", 523),
                   Phone("test2","testbrand2",22355, "teststorage2", 223)]


# add a phone in inventory
# ask the phone details from user before adding the phone to inventory
#TODO need to handle exceptions
#TODO how to prevent duplicate phone model numbers??
def add_phone():
    model = input("Enter the phone model: ")
    brand = input("Enter the phone brand: ")
    price = int(input("Enter the phone price: "))
    storage = input("Enter the phone storage: ")
    quantity = int(input("Enter the phone quantity: "))

    phone = Phone(model,brand, price, storage, quantity)

    phone_inventory.append(phone)

# view details of a phone
#TODO how do i show information of the phone that the user wants?
def view_phone_details():
    for phone in phone_inventory:
        print(f"Phone Model: {phone.get_model()}")
        print(f"Phone Brand: {phone.get_brand()}")
        print(f"Phone Storage: {phone.get_storage()}")
        print(f"Phone Price: {phone.get_price()}")
        print(f"Phone Quantity: {phone.get_quantity()}")
        print("\n")

# update detail of phones
def update_phone_details():
    model_number_to_update = input("Enter the phone model number to update: ")
    for phone in phone_inventory:
        if model_number_to_update == phone.get_model():
            new_model_number = input("Enter model number:")
            new_brand = input("Enter brand: ")
            phone.set_model(new_model_number)
            phone.set_brand(new_brand)
            print(f"{model_number_to_update} has been updated\n")
            return
    print(f"{model_number_to_update} not found in records\n")
             
# delete a phone
def delete_phone():
    model_number_to_delete = input("Enter the phone model to delete: ")
    for phone in phone_inventory:
        if model_number_to_delete == phone.get_model():
            phone_inventory.remove(phone)
            print(f"{model_number_to_delete} has been removed from the records....\n")
            return
        
    print(f"{model_number_to_delete} not found in the records....\n")
    
# how to allow users to do the operations?
# how to let the user use the program as much as they want?
# how to let the user exit the program?
def menu():
    while(True):
        print("Enter 1 to add phone: ")
        print("Enter 2 to view phone detail: ")
        print("Enter 3 to update phone detail: ")
        print("Enter 4 to remove a phone: ")
        print("Enter 5 to exit: ")
        option = int(input("Choose an option: "))
        if(option == 1):
            add_phone()
        elif(option == 2):
            view_phone_details()
        elif(option == 3):
            update_phone_details()
        elif(option == 4):
            delete_phone()
        elif(option == 5):
            print("Thank you, See You Again!!")
            break
        else:
            print("Enter the options from (1 to 5)\n")

if __name__ == '__main__':# to execute the file only when used
# when a module is imported in another module, 
# then the Python interpreter will assign the string with 
# the name of that module to the special variable __name__
    menu()