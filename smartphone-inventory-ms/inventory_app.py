from phone import Phone

#TODO how do i implement my inventory?
phone_inventory = [Phone("model","brand",223, "storage", 23)]


#TODO add a phone in inventory
#TODO ask the phone details from user before adding the phone to inventory
#TODO need to handle exceptions
def add_phone():
    model = input("Enter the phone model: ")
    brand = input("Enter the phone brand: ")
    price = int(input("Enter the phone price: "))
    storage = input("Enter the phone storage: ")
    quantity = int(input("Enter the phone quantity: "))

    phone = Phone(model,brand, price, storage, quantity)

    phone_inventory.append(phone)

# print(phone_inventory)


#TODO view details of a phone
#TODO how do i show information of the phone that the user wants?
def view_phone_details():
    for phone in phone_inventory:
        print(f"Phone Model: {phone.get_model()}")
        print(f"Phone Brand: {phone.get_brand()}")


#TODO update detail of phones
#TODO delete a phone

#TODO how to allow users to do the operations?
#TODO how to let the user use the program as much as they want?
#TODO how to let the user exit the program?
print("Enter 1 to add phone: ")
print("Enter 2 to view phone detail: ")
option = int(input("Choose an option: "))
if(option == 1):
    add_phone()
elif(option == 2):
    view_phone_details()

