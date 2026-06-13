#day 8 python
'''

stu_marks = 78
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >=60:
    print("B+")
elif stu_marks >= 50:
    print("C+")
elif stu_marks >= 35:
    print("pass")
else:
    print("faild")
    

a=8
b=567
c=90
if a > (b and c):
    print(a)
elif b > (a and c):
    print(b)
else:
    print(c)


SBI_bank ={"ATM PIN": "6600"}
pin = input("enter 4 disit ATM pin:")
if len(str(pin)) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("wel come to SBI ATM")
    else:
        print("invalid")
else:
    print("pls enter 4 disit pin")


any = "python"
an = [1,2,3,4]
so = (5,6,7,8)
for how in any:
    print(how)

range()
-------
range is in-built function use to genarate number in sequance manner.

syntax-->range(start,end,stop)
else in for
-----------
--->once the itterasions completed this else will be


for i in range(50,100,3):
    print(i)
else:
    print("code ended hear")

break statement
---------------
-->used to exit from the loop based on the condition

for i in range(1,10):
    if i == 3:
        break
    print(i)
    
continue
--------

for i in range(1,10):
    if i == 5:
        continue
    print(i)
pass
----

for i in range(1,10):
    if i == 3:
        pass
while
------
--->while is a for+if

'''
i = 1
while i < 5:
    print(i)
    i += 1 
    















































































