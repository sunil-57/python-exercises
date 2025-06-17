# TODO create a class name Phone
# with private attributes brand, model, model number, price, storage
# create setters and getters for the private attributes
class Phone:
    def __init__(self, model_number, model, brand, price, storage):
        self.__model_number = model_number
        self.__model = model
        self.__brand = brand
        self.__price = price
        self.__storage = storage
        