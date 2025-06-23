# TODO create a class name Phone
# with private attributes brand, model, model number, price, storage
# create setters and getters for the private attributes
class Phone:
    def __init__(self, model: str, brand: str, price: int, storage:str, quantity:int):
        self.__model = model
        self.__brand = brand
        self.__price = price
        self.__storage = storage
        self.__quantity = quantity
    
    
    def set_model(self, model:str):
        self.__model = model
        
    def set_brand(self, brand:str):
        self.__brand = brand
        
    def set_price(self, price:int):
        self.__price = price
        
    def set_storage(self, storage:str):
        self.__storage = storage
        
    def set_quantity(self, quantity:int):
        self.__quantity = quantity
    
    
    def get_model(self) -> str:
       return self.__model
   
    def get_brand(self) -> str:
       return self.__brand
   
    def get_price(self) -> int:
       return self.__price
   
    def get_storage(self) -> str:
       return self.__storage
   
    def get_quantity(self) -> int:
       return self.__quantity        
   
    def to_dict(self) -> dict:
        return {
            "model": self.__model,
            "brand": self.__brand,
            "price": self.__price,
            "storage": self.__storage,
            "quantity": self.__quantity
        }
    
    @staticmethod    
    def from_phone(self, item):
        return Phone(item["model"],
                     item["brand"],
                     item["price"],
                     item["storage"],
                     item["quantity"])