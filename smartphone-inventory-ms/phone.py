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
    
    
    def set_model(self, model):
        self.__model = model
        
    def set_brand(self, brand):
        self.__brand = brand
        
    def set_price(self, price):
        self.__price = price
        
    def set_storage(self, storage):
        self.__storage = storage
        
    def set_qunatity(self, quantity):
        self.__quantity = quantity
    
    
    def get_model(self):
       return self.__model
   
    def get_brand(self):
       return self.__brand
   
    def get_price(self):
       return self.__price
   
    def get_storage(self):
       return self.__storage
   
    def get_qunatity(self):
       return self.__quantity        