#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
a=0
b=1
numbers=int(input("Enter the number of Fibonacci sequence to generate: "))
if numbers==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,numbers):
        c=a+b
        a=b
        b=c
        print(c)
