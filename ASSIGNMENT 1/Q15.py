#15. Write a program that reads data from a CSV file and prints it to the console.
import csv

filepath=open("C://Users//Manshi Kharwar//Documents//EXCEL FILE//Student.csv - demo.csv.csv",'r')
csv_reader=csv.reader(filepath)
for row in csv_reader:
    print(row)