#16. Write a program in python that counts the frequency of each character in a string
# def count_frequency(string):
#  count={}
#
#  for letter in string:
#     if letter in count:
#         count[letter]+=1
#     else:
#          count[letter]=1
#
#
# # Get the input string from the user
# user_string = input("Enter a string: ")
#
#
# # Calculate the character frequency
# char_frequency = count_frequency(user_string)
# print("Character frequency:")
# for key, value in char_frequency.items():
#         print(f"{key}: {value}")


s=(input("Enter a string:"))
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    print(i,":",s.count(i))


