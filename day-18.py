#day-18
'''
opps
----

1.class
-------
-->a class is a blue-print or a template used to


2.object
--------
-->an object is an instance of a class


class stu_:
    def edu_(self):
         print("i am studying b.tech")
    def sport_(self):
        print("cricket")
        print("vall")
s1 = stu_()
s1 = sport_()



class stu_():
    name = 'teja'
    age = 46
s1 = stu_()
print(s1.name)
print(s1.age)
    
   
methods
--------
-->the functions defined inside the class is methods


class PFS_DA:
    def python(self):
        PFS_DA = 'batch_03'
        print('this PFS and DA batch03')

        
    def flask(self):
        PFS = 'batch_03'
        print('this is PFS batch03')
        
all_ = PFS_DA()
all_.python()
all_.flask()

constructor (__init__)
----------------------
--->constructor is a spacial method that is automatically called when an object is created


class ATM:
    def __init__(self,balance):
        self.balance = balance
        self.name = name

    def bal_check(self):
        print(f"{self.name}your total balance is {self.balance+700}")
        
    def name_(self):
        print(self.name)
        
card = ATM(balance = 50000,name='teja')
card.bal_check()
card.name_()

access specifiers
-----------------
1.publoc
--------
--> this ican be accessed from anywhere in the program


class stu_:
    _name = 'teja'
    
s1 = stu_()
print(s1._name)


2.proteacted
------------
-->this is represented using a single underscore(_)


private
---------
-->this is represented using a single underscore(__)


encapsulation
-------------
-->is the process of binding data and methods together
'''
class bank:
    def __init__(self, balance):
        self.__balance = balance

    def depo_(self, amount):
        self.__balance += amount
      
    def get_bala(self):
          return self.__balance
        
    
acc = bank(1000)
acc.depo_(10000)
print(acc.get_bala())















    

































