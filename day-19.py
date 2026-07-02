#day-19
'''
inheritance
-----------
-->this allows one class to aquire the properties and methods of another class..
type
1.single inheritance
--------------------
-->a class inherats from a single parent class..
2.multiple
----------
-->A child inherats from a parent class and another 
3.multi-level
-------------
-->
4.hierarchical inheratince
--------
5.hynride
---------
--->



1.
class father:
    def land(self):
        print("i am father have 5A")
class bhushan(father):
    def my_own(self):
        print('i have 2 A')
fam = bhushan()
fam.land()


2.

class father:
    def land(self):
        print("i am father have 5A")
class mother:
    def gold(self):
        print("my mother have 1kg G")
class son(father,mother):
    def mine(self):
        print('i have ntg')
all_ = son()
all_.land()
all_.gold()

3.

class grandfather:
    def land(self):
        print("my grandfather have 5A")
class father(grandfather):
    def flat(self):
        print("have flat of their BNG")
class son(father):
    def ntg(self):
        print("i both of their p")
all_ = son()
all_.land()
all_.flat()
all_.ntg()

4.

class father:
    def land(self):
        print("10 A land")

class bhushan(father):
    def mine(self):
        print("job")
class bibhuti(father):
    def bro(self):
        print("jobless")

bib = bibhuti()
bib.land()

so = bhushan()
so.land()
    


class A:
    def some(self):
        print('class A')

class B(A):
    def all(self):
        print('class B')

class C(A):
    def so(self):
        print('class C')

class D(B, C):
    def al_(self):
        print('class D')

how = D()
how.al_()




super() method
--------------
-->Super() is used to access method and contructor of the parent class from the clild vclass


class parent:
    def display(self):
        print('method parent')

class child(parent):
    def display(self):
        super().display()
        print('mathod child')

any_ = child()
any_.display()



'''
class person:
    def __init__(self,name):
        self.name = name
        
class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"name : {self.name}")
        print(f"roll no : {self.roll}")
any_ = stu_('bhushan', 1437)
any_.show()






