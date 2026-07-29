#1
""" def welcome():
    print('"Welcome to Python Programming!"')

welcome()
welcome()
welcome() """

#2
""" def greet(name):
    print(f'hello {name}')

greet('Lalit') """

#3
""" def add(a,b):
    return a+b
print(add(5,6)) """

#4
""" def largest(a,b,c):
    if a>b:
        if a>c:
            return a
    if b>a:
        if b>c:
            return b
    if c>a:
        if c>b:
            return c
print(f'{largest(2,4,6)} is Largest') """

#5
""" def calculate_interest(principal, time, rate=5):
    return (principal*time*rate)/100

print(f'Total interest = {calculate_interest(5000,1)}')
print(f'Total interest = {calculate_interest(5000,1,rate=10)}') """

#6
""" def numbers(*num):
    values = len(num)
    print(f'Number of values entered: {values}')
    add= sum(num)
    print(f'Sum of these values: {add}')

numbers(10,45,18,17,4) """

#7
""" def info(**data):
    print(f'Name: {data['name']}')
    print(f'Department: {data['department']}')
    print(f'Salary: {data['salary']}')
    print(f'{data}')

info(name='Lalit',department='CSE',salary=200000)"""

#8
""" var=10
def change():
    var=29
    print(var)
print(var)
change() """

#9
""" counter=1
def inc():
    global counter
    counter+=1
inc()
inc()
inc()
inc()
inc()
print(counter) """

#10
""" sqr= lambda x:x**2
print(sqr(4))

lar= lambda x,y: x if x>y else y
print(lar(34,100)) """