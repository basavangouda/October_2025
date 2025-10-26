# f=open("abc.txt",'w')
# print("File Name :",f.name)
# print("File Mode :",f.mode)
# print("is File Readable :",f.readable())
# print("is File Writable :",f.writable())
# print("is File closed :",f.closed)
# f.close()
# print("is File closed :",f.closed)

#Program 1:
# f=open("xyz.txt",'w')
# f.write("QACircle\n")
# f.write("Software\n")
# f.write("Training\n")
# f.write("Academy")
# print("Data written to the file successfully")
# f.close()
#
# #Program 2:
# f=open("abc.txt",'w')
# l=["QACircle ","Software ","Training ","Academy"]
# f.writelines(l)
# print("List of lines written to the file successfully")
# f.close()

# #Ex 1 : read() ===> To read total data from the file
# f=open("xyz.txt",'r')
# data=f.read()
# print(data)
# f.close()
#
# print("************************")
# #Ex 2 : read(n) ====> To read ‘n’ characters from file
# f=open("xyz.txt",'r')
# data=f.read(10)
# print(data)
# f.close()
#
# print("************************")
# #Ex 3 : readline() ===> To read only one line
# f=open("xyz.txt",'r')
# line1=f.readline()
# print(line1,end='')
# line2=f.readline()
# print(line2,end='')
# line3=f.readline()
# print(line3,end='')
# line4=f.readline()
# print(line4,end='')
# f.close()
#
# print("************************")
# #Ex 4 : readlines() ===> To read all lines into list
# f=open("xyz.txt",'r')
# lines=f.readlines()
# print(lines)
# for line in lines:
#     print(line,end='')
# f.close()

# with open("abc.txt",'w') as f:
#     f.write("Hello\n")
#     f.write("Good Morning\n")
#     f.write("Welcome to the Python Class")
#     print("Is file closed :",f.closed)
# print("Is file closed :",f.closed)

# import os,sys
# fname=input("Enter the file name")
# if os.path.isfile(fname):
#     print("File Exist:",fname)
#     f=open(fname,"r")
# else:
#     print("File Does not exist",fname)
#     sys.exit(0)
# print("The content of the file")
# data=f.read()
# print(data)

# import os,sys
# fname=input("Enter the file name")
# if os.path.isfile(fname):
#     print("File Exist:",fname)
#     f=open(fname,"r")
# else:
#     print("File Does not exist",fname)
#     sys.exit(0)
#
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
#
# print("The number of lines :",lcount)
# print("The number of Characters :",ccount)
# print("The number of Words:",wcount)

# f1=open("C:/Users/dell/Documents/123.jpg",'rb')
# f2=open("new.jpg",'wb')
# bytes=f1.read()
# print(bytes)
# f2.write(bytes)
# print("New Image is available with name new.jpg")

# import csv
# with open("emp.csv","w",newline='') as f:
#     w=csv.writer(f) #retuen csv writer object
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n=int(input("Enter the number of Employee's"))
#     for i in range(n):
#         eno=input("Enter the Employee No:")
#         ename=input("Enter the Employee Name:")
#         esal=input("Enter the Employee Salary:")
#         eaddr=input("Enter the Employee Address:")
#         w.writerow([eno,ename,esal,eaddr])
# print("Total employee data written to csv file")

# import csv
# f=open("emp.csv",'r')
# r=csv.reader(f) #Return the reader Object
# data=list(r)
# print(data)
# for line in data:
#     for word in line:
#         print(word,"\t\t\t", end='')
#     print()

# #Writing Data to the excel file
# import openpyxl
#
# wb = openpyxl.Workbook()
#
# sheet=wb.active
#
# c1=sheet.cell(row=1,column=1,value="Hello")
#
# c11=sheet.cell(row=2,column=1,value="Good Morning")
#
# c2=sheet.cell(row=1,column=2,value="Hi")
#
# c22=sheet.cell(row=2,column=2,value="Bye")
#
# wb.save("sample.xlsx")


# #case 2
# import openpyxl
# file="D:\\QACircle.xlsx"
# workbook=openpyxl.load_workbook(file)
# sheet=workbook['Sheet1']
#
# #Count the number of rows
# rows=sheet.max_row
# print(rows)
#
# #Count Number of columns
# column=sheet.max_column
# print(column)
#
# #Write all the row and Column data
#
# for r in range(1,rows+1):
#     for c in range(1,column+1):
#         sheet.cell(r,c).value="QACircle Software Training Academy"
#
# workbook.save(file)

# #case 2
# import openpyxl
# file="D:\\QACircle.xlsx"
# workbook=openpyxl.load_workbook(file)
# sheet=workbook['Sheet1']
#
# #Count the number of rows
# rows=sheet.max_row
# print(rows)
#
# #Count Number of columns
# column=sheet.max_column
# print(column)
#
# #Write all the row and Column data
#
# for r in range(1,rows+1):
#     for c in range(1,column+1):
#         print(sheet.cell(r,c).value,end=' ')
#     print()


