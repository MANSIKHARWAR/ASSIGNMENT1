 # 3. Write a python program that calculates the factorial of a given number
def factorial_recursive(num):
  if num==0 or num==1:
      return 1
  elif num<0:
      print("cannot be negtive number")
  else :
      return num*factorial_recursive(num-1)

num=int(input("Enter a number: "))
result=factorial_recursive(num)
print(f"the factorial of {num} is {result}")
