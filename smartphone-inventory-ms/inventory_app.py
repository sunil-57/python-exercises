from phone import Phone

#TODO how do i implement my inventory?
phone_inventory = []


#TODO add a phone in inventory
#TODO ask the phone details from user before adding the phone to inventory
#TODO 
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
for phone in phone_inventory:
    print(f"Phone Model: {phone.get_model()}")
    print(f"Phone Brand: {phone.get_brand()}")


#TODO update detail of phones
#TODO delete a phone

#TODO how to allow users to do the operations?