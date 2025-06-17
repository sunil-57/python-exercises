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


#creating object of the class
teacher1 = Teacher("Sunil", 25) 

#accessing the private attributes of class is not allowed
# print(teacher1.age)
# print(teacher1.name)

#calling the function of the class
teacher1.give_assignment()
teacher1.set_name("Janak")
print(teacher1.get_name())