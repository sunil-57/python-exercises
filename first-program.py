#to check the sum of two numbers 
#provided by user is even or not using functions
def add(a, b):
    return a+b
def check_even(number):
    if number%2 == 0:
        return True
    else:
        return False

#TODO ask two numbers from users
first_number = int(input("Enter first number\n"))
second_number = int(input("Enter second number\n"))

#TODO find the sum using add function
# sum = add(first_number, second_number)
#TODO check the sum is even or not
if check_even(add(first_number, second_number)):
    print("Even")
else:
    print("Odd")