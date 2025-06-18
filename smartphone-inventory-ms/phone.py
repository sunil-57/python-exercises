# TODO create a class name Phone
# with private attributes brand, model, model number, price, storage
# create setters and getters for the private attributes
class Phone:
    def __init__(self, model, brand, price, storage, quantity):
        self.__model = model
        self.__brand = brand
        self.__price = price
        self.__storage = storage
        self.__quantity = quantity
        
    
        