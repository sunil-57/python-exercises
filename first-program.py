try:
    age = int(input("Enter your age: "))
    #operators
    # == equals to
    # != not equals to
    # < less than
    # > greater than
    # <= less than equal to
    # >= greater than equal to
    if age < 15:
        print(f"{age} is minor")
    elif age >= 15:
        print(f"{age} is old")
    else:
        print("enter a proper age")
except:
    print("please give numbers")