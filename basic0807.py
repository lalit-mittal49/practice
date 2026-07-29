#1
""" name = 'Rahul'
age = 22
city = 'Mohali'
college = 'GNDEC'
print("-----Student Information-----")
print('Name : '+name)
print('Age : ' +str(age))
print('City : '+city)
print('College : '+college)
print(' ') """

#2
""" empName = 'Aman'
empID = 1023
department = 'IT'
salary = 45000
print('Employee Name : '+empName)
print('Employee ID : '+ str(empID))
print('Department : '+department)
print('Salary : '+ str(salary))
print(' ') """

#3
""" name = 'Rahul'
age = 22
height = 5.8
isStudent = True
print(name)
print(type(name))
print(age)
print(type(age))
print(height)
print(type(height))
print(isStudent)
print(type(isStudent))
print(' ') """

#4
""" name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')
print('Welcome'+ str(name))
print('Your Details')
print('Name :'+ str(name))
print('Age : ' +str(age))
print('City : '+ city)
print(' ') """

#5
""" favoriteMovie = input('My favorite movie is ')
favoriteFood = input('My favorite food is ')
favoriteColor = input('My favorite color is ')
print(' ') """

#6
""" firstNumber  = int(input('First Number  :'))
secondNumber = int(input('Second Number :'))
sum = firstNumber+secondNumber
print(sum)
print(' ') """

#7
""" studentName = input('Enter name ')
rollNumber = int(input('enter roll no '))
englishMarks = int(input('enter english marks '))
mathMarks = int(input('enter math marks '))
scienceMarks = int(input('enter science marks '))
print('Student Report \n',\
'Name      : '+studentName +'\n',\
'Roll No   : ',(rollNumber),'\n',\
' '+'\n',\
'English   : ',(englishMarks),'\n',\
'Math      : ',(mathMarks),'\n',\
'Science   : ',(scienceMarks),'\n') """

#8
""" age = int("25")
salary = float("35000.75")
number = str(100)
print(age)
print(type(age))
print(salary)
print(type(salary))
print(number)
print(type(number)) """

#9
""" productName = input('Enter Product Name- ')
quantity = int(input('Enter Quantity- '))
priceperItem = int(input('Enter Price per Item- '))
cost = quantity*priceperItem
print('\nTotal cost = ', cost) """

#10
""" print("====================================\n          STUDENT ID CARD\n====================================")
print(" ")
name = input('Name      : ')
age = input('Age       : ')
course = input('Course    : ')
college = input('College   : ')
city = input('City      : ')
phoneNumber = input('Phone     : ') """

#11
""" studentName = input('Enter Student Name- ')
courseName = input('Enter Course Name- ')
registrationFee = int(input('Enter Registration Fee- '))
tuitionFee = int(input('Enter Tuition Fee- '))
labFee = int(input('Enter Lab Fee- '))
cost = registrationFee+tuitionFee+labFee
print('=========================================\n           NETSQUARE SOFTWARES\n              FEE RECEIPT\n=========================================\n\nStudent Name : ',studentName,'\nCourse       : ',courseName,'\nRegistration : ',registrationFee,'\nTuition Fee  : ',tuitionFee,'\nLab Fee      : ',labFee,'\n\n-----------------------------------------\nTotal Fee    : ',cost,'\n=========================================')
 """

#12
""" customerName = input('Enter Customer Name- ')
foodItem1Price = int(input('Enter Food Item 1 Price- '))
foodItem2Price = int(input('Enter Food Item 2 Price- '))
foodItem3Price = int(input('Enter Food Item 3 Price- '))
gstPercentage = int(input('Enter GST Percentage- '))
totalFoodBill = foodItem1Price+foodItem2Price+foodItem3Price
gstAmount = int((totalFoodBill*gstPercentage) / 100)
finalBill =  totalFoodBill+gstAmount
totalFoodBill = foodItem1Price+foodItem2Price+foodItem3Price
print('\n\nCustomer Name : ',customerName,'\n\nFood Total : ',totalFoodBill,'\nGST (',gstPercentage,'%)  :',gstAmount,'\n-------------------------\nFinal Bill : ',finalBill)
 """

#13
""" employeeName = input('Enter Employee Name- ')
basicSalary = int(input('Enter Basic Salary- '))
HRA = int(input('Enter HRA- '))
bonus = int(input('Enter Bonus- '))
taxDeduction = int(input('Enter Tax Deduction- '))
grossSalary = basicSalary + HRA + bonus
netSalary = grossSalary - taxDeduction
print('==================================\n          SALARY SLIP\n==================================\n\nEmployee Name : ',employeeName,'\nBasic Salary  : ',basicSalary,'\nHRA           : ',HRA,'\nBonus         : ',bonus,'\nTax Deduction : ',taxDeduction,'\n\n----------------------------------\nGross Salary  : ',grossSalary,'\nNet Salary    : ',netSalary,'\n==================================')
 """

#14
""" studentName = input('Enter Student Name- ')
rollNumber = int(input('Enter Roll Number- '))
marksEnglish = int(input('Enter Marks in English- '))
marksMathematics = int(input('Enter Marks in Mathematics- '))
marksScience = int(input('Enter Marks in Science- '))
marksComputer = int(input('Enter Marks in Computer- '))
totalMarks = marksEnglish+marksMathematics+marksScience+marksComputer
percentage = (totalMarks/400)*100
print('=================================\n        STUDENT RESULT\n=================================\n\n')
print('\nName        : ',studentName)
print('\nRoll Number : ',rollNumber)
print('\nEnglish     : ',marksEnglish)
print('\nMath        : ',marksMathematics)
print('\nScience     : ',marksScience)
print('\nComputer    : ',marksComputer)
print('\n\n---------------------------------\nTotal Marks : ',totalMarks)
print('\nPercentage  : ',percentage)
print('\n=================================') """

#15
""" name = input('Enter Traveller      : ')
hotelCostPerNight = input('Enter Hotel Cost per Night- ')
numberOfNights = input('Enter Number of Nights- ')
foodExpensePerDay = input('Enter Food Expense per Day- ')
numberOfDays = input('Enter Number of Days- ')
travelCost = input('Enter Travel Cost- ')
shoppingExpense = input('Enter Shopping Expense- ')
hotelExpense = hotelCostPerNight*numberOfNights
foodExpense = foodExpensePerDay*numberOfDays
grandTotalTripCost = hotelExpense+foodExpense+shoppingExpense+travelCost
print('========================================\n          TRIP EXPENSE REPORT\n========================================\n\nTraveller      : ',name)
print('\nHotel Expense  : ',hotelExpense)
print('\nFood Expense   : ',foodExpense)
print('\nTravel Expense : ',travelCost)
print('\nShopping       : ',shoppingExpense)
print('\n\n----------------------------------------\nTotal Expense  : ',grandTotalTripCost)
print('========================================') """