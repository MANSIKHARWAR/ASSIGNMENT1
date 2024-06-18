# 12. Write a python program that calculates the sum of the digits of a given number.
numbers=int(input("Enter a number: "))
sum=0
while (numbers>0):
 remainder=numbers%10
 sum=sum+remainder
 numbers=numbers//10
 print("sum of th digit",sum)




