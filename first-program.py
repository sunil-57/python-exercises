class Teacher:#creating a class
    def __init__(self, name, age):#initialzing the attributes of the class
        self.__name = name  #making the attributes private
        self.__age = age

    #using setter methods to set the values in private attributes
    def set_name(self, name):
        self.__name = name
    
    #using getter methods to get the values of private attributes
    def get_name(self):
        return self.__name
    
    def give_assignment(self): #creating the behaviour of a class
        print("Complete the assignment")

class Math_Teacher(Teacher):#inheriting the Parent class (Teacher)
    def __init__(self, name, age, strict):
        super().__init__(name, age)# using the init method of parent class
        self.strict = strict
    
    def set_strict(self, strict):
        self.__strict = strict
        
    def get_strict(self):
        return self.__strict
    
    def give_assignment(self): #polymorphism method overriding
        print("Complete the Formula")
        
        
class English_Teacher(Teacher):
    def __init__(self, name, age, polite):
        super().__init__(name, age)
        self.__polite = polite 
    
#creating object of the class
math_teacher1 = Math_Teacher("Sunil", 25, "Very Strict")

#accessing the private attributes of class is not allowed
# print(teacher1.age)
# print(teacher1.name)

#calling the function of the class
print(math_teacher1.get_name())
math_teacher1.give_assignment()