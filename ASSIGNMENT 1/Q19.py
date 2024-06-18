# 19. Write a python program that removes all punctuation from a given string
import re
string=input("Enter a string: ")
string=re.sub('[^A-Za-z]'," ",string)
print(string)
