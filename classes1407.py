#1
""" class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print(f'Name - {self.name}\nAge - {self.age}\nCourse - {self.course}')

student1= student('Lalit',20,'CSE')
student2= student('Karan',21,'CSE')
student1.display()
student2.display() """

#2
""" class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def show_details(self):
        print(f'Brand : {self.brand}')
        print(f'Model : {self.model}')
        print(f'Price : {self.price}\n')
car1 = car('toyota',2014,400000)
car2 = car('honda',2015,180000)
car3 = car('Jaguar',2022,5000000)
car1.show_details()
car2.show_details()
car3.show_details() """

#3
""" class mobile:
    def __init__(self,brand,Ram,storage):
        self.brand = brand
        self.Ram = Ram
        self.storage = storage
    def call(self):
        print(f'{self.brand} is calling...')
    def camera(self):
        print(f'{self.brand} camera opened...')
mobile1=mobile('Samsung',16,256)
mobile1.call()
mobile1.camera() """

#4
""" class book:
    def __init__(self,Title,Author,price):
        self.Title = Title
        self.Author = Author
        self.price = price
    def display(self):
        print(f'Title : {self.Title}')
        print(f'Author : {self.Author}')
        print(f'Price : {self.price}\n')
book1=book("10 questions",'me',10000)
book1.display() """

#5
""" class Laptop:
    def __init__(self,Brand,Processor,Ram,price):
        self.Brand = Brand
        self.Processor = Processor
        self.Ram = Ram
        self.price = price
    def display(self):
        print(f'Brand : {self.Brand}')
        print(f'Processor : {self.Processor}')
        print(f'RAM : {self.Ram}')        
        print(f'Price : {self.price}\n')
Laptop1=Laptop("Acer",'i7',16,80000)
Laptop2=Laptop("Acer",'i7',32,90000)
Laptop3=Laptop("Lenovo",'i5',8,70000)
Laptop1.display()
Laptop2.display()
Laptop3.display() """

#6
""" class student:
    def __init__(self,name,marks):
            self.name=name
            self.marks=marks
    def display(self):
        print(f'Name - {self.name}\nMarks - {self.marks}')
    def result(self):
        if self.marks >=40:
            print('PASS')
        else:
            print('FAil')
student1=student('Karan',90)
student2=student('Lalit',95)
student1.display()
student1.result()
student2.display()
student2.result() """

#7
""" class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f'Name - {self.name}\nSalary - {self.salary}')
    def bonus(self):
        if self.salary>=50000:
            bonus=self.salary*(20/100)
            self.salary+=bonus
            print(f'Bonus credited : {bonus}')
        else:
            bonus=self.salary*(10/100)
            self.salary+=bonus
            print(f'Bonus credited : {bonus}')
emp1=employee('Lalit',1000000)
emp1.display()
emp1.bonus() """

#8
""" class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(f'Area = {self.length*self.width}')
    def perimeter(self):
        print(f'Perimeter = {(self.length+self.width)*2}')
rec1=rectangle(10,20)
rec1.area()
rec1.perimeter() """

#9
""" class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f'Area = {self.radius*self.radius*3.14}')
    def circumference(self):
        print(f'Circumference = {(self.radius*3.14)*2}')
circle1=circle(10)
circle1.area()
circle1.circumference() """

#10
""" class BankAccount:
    def __init__(self,AHname,Balance):
        self.AHname=AHname
        self.Balance=Balance
    def show_balance(self):
        print(f'Account Holder Name - {self.AHname}\nBalance - {self.Balance}\n')
    def deposit(self,amount):
        self.amount=amount
        self.Balance+=amount
        print(f'Updated balance = {self.Balance}\n')
    def withdraw(self,amount):
        self.amount=amount
        if self.Balance>=amount:
            self.Balance-=amount
            print(f'Withdrawal Successfull !!\nUpdated balance = {self.Balance}\n')
        else:
            print(f'Insufficient balance\n')
ba1=BankAccount('Lalit',500000)
ba1.show_balance()
ba1.deposit(9000)
ba1.withdraw(1200)
ba1.show_balance() """

#11
""" class student:
    def __init__(self,name,roll_no,course,marks):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        self.marks=marks
    def display(self):
        print(f'Name - {self.name}')
        print(f'Roll No. -{self.roll_no}')
        print(f'Course - {self.course}')
        print(f'Marks - {self.marks}')
        print(f'\n')
std1=student('Lalit',18,'CSE',95)
std2=student('Karan',52,'CSE',85)
std3=student('Ram',85,'ECE',78)
std4=student('abc',98,'CE',60)
std5=student('Ravi',42,'CE',70)
std6=student('Nonu',70,'CE',79)

stdList=[std1,std2,std3,std4,std5,std6]
for student in stdList:
    student.display() """

#12
""" class book:
    def __init__(self,Id,Title,Author,price):
        self.Id=Id
        self.Title = Title
        self.Author = Author
        self.price = price
    def display(self):
        print(f'Book ID - {self.Id}')
        print(f'Title - {self.Title}')
        print(f'Author - {self.Author}')
        print(f'Price - {self.price}')
        print('\n')
book1=book(300,'qwe','rty',500)
book2=book(301,'asd','fgh',600)
book3=book(302,'zxc','vbn',200)
book4=book(303,'poi','lkj',100)
book5=book(304,'fgh','mnb',900)
book_list=[book1,book2,book3,book4,book5]
searchId=301
for book in book_list:
    if searchId== book.Id:
        print(f'{book.display()}')
        break """

#13
""" class employee:
    def __init__(self,id,name,dep,salary):
        self.name=name
        self.salary=salary
        self.dep=dep
        self.id=id
    def display(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Department : {self.dep}')
        print(f'Salary : {self.salary}\n')
emp1=employee(201,'qwe','cse',10000)
emp2=employee(205,'asd','ce',60000)
emp3=employee(210,'zxc','ce',20000)
emp4=employee(215,'poi','cse',80000)
emp5=employee(220,'fgh','ce',50000)
emp_lst=[emp1,emp2,emp3,emp4,emp5]
for employee in emp_lst:
    if employee.salary>50000:
        employee.display()"""

#14
""" class product:
    def __init__(self,id,name,quantity,price):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.id=id
    def display(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Quantity : {self.quantity}')
        print(f'Price : {self.price}\n')
    def stock_value(self):
        value=self.quantity*self.price
        return value
pro1=product(201,'qwe',5,10000)
pro2=product(205,'asd',50,60000)
pro3=product(210,'zxc',80,20000)
pro4=product(215,'poi',10,80000)
pro5=product(220,'fgh',14,50000)
pro_lst=[pro1,pro2,pro3,pro4,pro5]
total_value=0
for product in pro_lst:
    total_value+=product.stock_value()
print(f'Total stock value = {total_value}') """

#15
""" class student:
    def __init__(self,name,roll_no,course,marks):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        self.marks=marks
    def display(self):
        print(f'Name - {self.name}')
        print(f'Roll No. -  {self.roll_no}')
        print(f'Course - {self.course}')
        print(f'Marks - {self.marks}')
    def grade(self):
        if self.marks>=90:
            grad='A'
            return grad
        if 75<=self.marks<=89:
            grad='B'
            return grad
        if 50<=self.marks<=74:
            grad='C'
            return grad
        if 50>self.marks:
            grad='Fail'
            return grad
std1=student('Lalit',18,'CSE',95)
std2=student('Karan',52,'CSE',85)
std3=student('Ram',85,'ECE',78)
std4=student('abc',98,'CE',60)
std5=student('Ravi',42,'CE',70)
std6=student('Nonu',70,'CE',79)

stdList=[std1,std2,std3,std4,std5,std6]
for student in stdList:
    student.display()
    print(f"Student's Grade: {student.grade()}\n")
highest=0
for student in stdList:
    if highest<student.marks:
        highest=student.marks
print(f'Highest marks: {highest}')
for student in stdList:
    if student.marks==highest:
        student.display()
sum=0
for student in stdList:
    sum+=student.marks
average=sum/len(stdList)
print(f'\nAverage is {average}') """
