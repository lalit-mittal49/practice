#2
""" class animal:
    def eat(self):
        print('Animals eat')
class dog(animal):
    def bark(self):
        print('Dog barks')
class cat(animal):
    def meow(self):
        print('Cat meow')
class elephant(animal):
    def trumpet(self):
        print('elephant trumphets')

mycat=cat()
mydog=dog()
myelephant=elephant()

mycat.eat()
mycat.meow()
mydog.eat()
mydog.bark()
myelephant.eat()
myelephant.trumpet() """

#3
""" class creditCard:
    def pay(self):
        print('Paid through Creditcard')
class UPI:
    def pay(self):
        print('Paid through UPI')
class cash:
    def pay(self):
        print('Paid through cash')
cc=creditCard()
upi=UPI()
mycash=cash()
cc.pay()
upi.pay()
mycash.pay() """

#4
""" class SmartTV:
    def __init__(self):
        self.__volume=20
    def increase_volume(self):
        if self.__volume==100:
            print('Volume is full !!')
        else:
            self.__volume+=1
            print(f'Volume : {self.__volume}')
    def decrease_volume(self):
        if self.__volume==0:
            print('Mute !!')
        else:
            self.__volume-=1
            print(f'Volume : {self.__volume}')
    def show_volume(self):   
        print(f'volume is {self.__volume}') 
myTV= SmartTV()
myTV.show_volume()
myTV.decrease_volume()
myTV.decrease_volume()
myTV.decrease_volume()
myTV.decrease_volume()
myTV.increase_volume()
myTV.show_volume() """

#5
""" students = ["Aria", "Ethan", "Liam", "Maya", "Noah"]
f = open("attendance.txt","w+")
for i in range(0,len(students)):
    f.write(f"{students[i]}\n")
f.seek(0)
print(f.read()) """

#6
""" f= open("products.csv","x")
numItems= int(input('Enter number of products: '))
totalvalue=0
f.write('Name , ID , Price , Quantity\n')
for i in range(0,numItems):
    f.write(f"{input('Enter product name: ')},     ")
    f.write(f"{int(input('Enter product ID: '))},   ")
    price= float(input('Enter product price: ')) 
    f.write(f'{price},    ')
    quantity=int(input('Enter product quantity: '))
    f.write(f'{quantity},    \n')
    totalvalue=(price*quantity)+totalvalue
f= open("products.csv","r")    
print(f'{f.read()}')
print(f'Total value : {totalvalue}')
 """

#7
""" class patient:
    def __init__(self,name,id,disease,age):
        self.id=id
        self.name=name
        self.disease=disease
        self.age=age
    def display(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Disease : {self.disease}')
        print(f'Age : {self.age}\n')
p1=patient('lkj',14,'qwe',10)
p2=patient('mnb',14,'ytu',45)
p3=patient('xcv',78,'zxc',23)
p4=patient('asd',98,'cbv',35)
p5=patient('zxc',41,'ghj',46)
p_lst=[p1,p2,p3,p4,p5]
f=open('patients.csv',"w+")
f.write('Name , ID , Disease , Age')
for patient in p_lst:
    f.write(f'{patient.name},   ')
    f.write(f'{patient.id},   ')
    f.write(f'{patient.disease},   ')
    f.write(f'{patient.age},   \n')
f.seek(0)
print(f.read())
for patient in p_lst:
    patient.display() """

#8
""" f=open('movie.csv',"x")
class movie:
    def __init__(self,name,id,Language,Rating):
        self.id=id
        self.name=name
        self.Language=Language
        self.Rating=Rating
    def display(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Language : {self.Language}')
        print(f'Rating : {self.Rating}')
    def is_hit(self):
        if self.Rating>=8:
            return'Movie is Hit'
        else:
            return 'Average movie'
m1=movie('lkj',14,'qwe',10)
m2=movie('mnb',14,'ytu',5)
m3=movie('xcv',78,'zxc',9)
m4=movie('asd',98,'cbv',3)
m5=movie('zxc',41,'ghj',6)
m_lst=[m1,m2,m3,m4,m5]
f=open('movie.csv',"w+")
f.write('Name , ID , Language , Rating\n')
for movie in m_lst:
    f.write(f'{movie.name},   ')
    f.write(f'{movie.id},   ')
    f.write(f'{movie.Language},   ')
    f.write(f'{movie.Rating},    \n')
    f.write(f'{movie.is_hit()}\n\n')
f.seek(0)
print(f.read())
for movie in m_lst:
    movie.display()
    movie.is_hit()
    print('\n') """
