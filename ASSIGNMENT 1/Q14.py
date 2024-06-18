#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines=[]
print("enter multiple line of text(press enter after finish the ine) :")
while True:
    line=input()
    if line=="":
        break # break the line and leave one line
        line.append(lines)
print(" you entered these line")
for i in line:
    print(line)



