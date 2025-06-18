from phone import Phone

#how do i implement my inventory?
phone_inventory = [Phone("model","brand",223, "storage", 23)]


# add a phone in inventory
# ask the phone details from user before adding the phone to inventory
#TODO need to handle exceptions
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


#TODO update detail of phones
#TODO delete a phone

# how to allow users to do the operations?
# how to let the user use the program as much as they want?
# how to let the user exit the program?
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
    elif(option == 5):
        break
    else:
        print("Enter the options from (1 to 5)\n")