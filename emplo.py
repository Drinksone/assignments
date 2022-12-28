import csv                                                   #import csv module
import datetime                                              #import datetime module

#write in csv file
with open('example.csv','w',newline='') as myfile:
    w=csv.writer(myfile)
    w.writerow(['emp_name','emp_dob','emp_salary'])           #write field which we required
    while True:
        emp_name=input("enter the employee name:")
        emp_dob=str(input("enter date of birth for employee(YYYY-DD-MM):"))
        birthdate_year=int(input("employee birth year"))
        today_date=datetime.date.today()
        today_year=int(datetime.date.today().year)
        emp_salary=int(input("enter employee salary:"))
        age = today_year - birthdate_year
        print("employee age is :", age)
        w.writerow([emp_name,emp_dob,emp_salary])
        option=input("do you want to insert more data [yes/no]:")
        if option.lower()=='no':
           break
print("total employee data:")                                     #final data

#read csv file
with open('example.csv','r') as myfile:
    r=csv.reader(myfile)
    data=list(r)
    for row in data:
        for column in row:
            print(column,end='')
            print()