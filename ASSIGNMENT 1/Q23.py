# 23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
print("Temperature Conversion Program")
print("1: Convert Celsius to Fahrenheit")
print("2: Convert Fahrenheit to Celsius")
choice=int(input("Enter  your choice from 1 and 2: "))

match choice:
    case 1:
        Celisus=float(input("Enter Celsius: "))
        fahrenheit=(Celisus*9/5)+32
        print( f" {Celisus} degrees is equal to {fahrenheit} degree Fahrenheit")
    case 2:
        Fahrenheit=float(input("Enter fahrenheit: "))
        celisus=(Fahrenheit-32)*5/9
        print( f" {celisus} degrees is equal to {Fahrenheit} degree Celisus")
    case _:
        print("Invalid choice")