#day-9 of py.
'''

-->this is debugging   statement 



num = 10
assert num >= 15, "age must be grater then or euale to 15"
print("TRUE")


functions
---------
-->a functoin is block of code which only execute when it is called functions
-->you can pass data, known as perameters into a functions
-->to avoid repeated lines in code
-->def keword function_name(parameters):
--------------------------------------
--------------------------------------
function_mane(agruments)


num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} even")
    else:
        print(f"{num} odd")
even(num)
even(109)
   

ways to pass ageruments
-----------------------
1.requiredment code
2nd required
---> by defult, values is define at parameters even tho it will taken from arguments

def even(name = "bhushan",age = 89, sal = 10):
    print(name)
    print(age)
    print(sal)
even("balaji",89,75000)

key bordlength agruments
------------------------
--->we can send argument with key=value syntax. by this,the order of arguments
dose not mater..


def even(name = name,age ,sal):
    print(name)
    print(age)
    print(sal)
even("balaji",age = 89,sal = 75000)

variable length arguments
--------------------------
-->adding a star(*) before the perametar in the functions, recive atripul of
arguments and can access item with indexers


def even(*name):
    print(name[1])
even("bhushan","teja","prem","ravi")



name = "bhushan"
def even(any):
    print(any)
even(name)



for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


'''


def even(name = name,age,sal):
    print(name)
    print(age)
    print(sal)
even("balaji",age = 89,sal = 75000)




        
   
    


































































     










