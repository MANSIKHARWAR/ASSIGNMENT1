# 20. Write a python program that takes a list of numbers and returns their sum.
# list=[12,43,32,21]
# sum=list[0]+list[1]+list[2]+list[3]
# print("sum of the list element : ",sum)


number=list(map(int,input("Enter the number: ").split()))
total_sum=sum(number)
print("The total sum is: ",total_sum)