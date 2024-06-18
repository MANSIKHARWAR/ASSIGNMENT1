#5. Write a program that takes a string input from the user and writes it to a text file.

samplefile=open("C:/Users/Manshi Kharwar/Desktop/IGDTUW PYTHON AND ML/New Text Document.txt",'w')
A=input("enter any content: ")
samplefile.write(A)
samplefile.close()