#function with output = return

# def function(text):
#     return text.title()

# output = function("siBanKar")
# print(output)

#leap year code
# def leap_year(year):
#     """this is a docstring, function will give True or False based on leap year"""
#     if year % 100 == 0 and year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         return False


# provided_year = int(input("please provide a year\n"))

# print(leap_year(provided_year))

### calculator
def addition(n1,n2):
    return n1+n2
def substraction(n1,n2):
    return n1-n2
def multipication(n1,n2):
    return n1*n2
def divition(n1,n2):
    return n1/n2

# def calculation(n1,n2,opt):
#     if opt == "+":
#         return addition(n1,n2)
#     elif opt == "-":
#         return substraction(n1,n2)
#     elif opt == "*":
#         return multipication(n1,n2)
#     elif opt == "/":
#         return divition(n1,n2)

operations = {
    "+":addition,
    "-":substraction,
    "*":multipication,
    "/":divition
}

def calculation():
    first_num = float(input("Whats the first number: "))
    is_next_calculation = True

    while is_next_calculation:
        for symbol in operations:
            print(symbol)
        operation = input("pick an operation: ")
        second_num = float(input("Whats the second number: "))

        calculated_value = operations[operation](first_num,second_num)
        print(f"{first_num} {operation} {second_num} = {calculated_value}")
        continue_input = input(f"tupe y to continue with {calculated_value} or type n for new calculation")

        if continue_input == "y":
            first_num = calculated_value
        elif continue_input == "n":
            is_next_calculation = False
            calculation()
            




