#day-21
'''
error handling
--------------
try block
----------
-->the try block, test a block of code for error
except block
------------
-->the except block let hand if the code contain errors

else block
----------
-->the else block will be excuted, if try block has no error in the code...
finally block
-------------
-->this will be excuted try block contain error or not...


try:
    print(10/0)
except:
    print('this will handle zerodivisionerror')
 

try:
    print("hai")
except:
    print('this will handle zerodivisionerror')
else:
    print("no error")




try:
    print(5+"py")
except NameError:
    print('this will handle NameError')
else:
    print("no error")


try:
    print(5+"py")
    print(a)
except TypeError:
    print('this will handle TypeError')
except NameError:
    print('this will handle NameError')
else:
    print("no error")
    
'''
try:
    print("hai")
except:
    print("Error")
else:
    print("no error")
finally:
    print('the end')













