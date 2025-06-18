from phone import Phone

#TODO how do i implement my inventory?
phone_inventory = []


#TODO add a phone in inventory
#TODO ask the phone details from user before adding the phone to inventory
phone = Phone("S20","Samsung", 50000, "32 GB", 30 )
phone1 = Phone("S23","Samsung", 70000, "32 GB", 30 )
phone_inventory.append(phone)
phone_inventory.append(phone1)

# print(phone_inventory)


#TODO view details of a phone
#TODO how do i show information of the phone that the user wants?
for phone in phone_inventory:
    print(f"Phone Model: {phone.get_model()}")
    print(f"Phone Brand: {phone.get_brand()}")


#TODO update detail of phones
#TODO delete a phone

#TODO how to allow users to do the operations?