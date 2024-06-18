# 13. Write a program that asks the user for their birth year and calculates their age.

from datetime import date

birthdate=int(input("Enter your year of birth: "))
today=date.today().year # current date
birth_date=today-birthdate
print("yor current age is",birth_date)
