#day-22
'''
file handling
-------------
-->file handler is an object of file to maintain several function of file like,
creating, reading,updateing and deleting the file...

open a file
-----------
1.open()
2.with open()

modes
-----
'r'-->is used to reading the file, error if else dose not exist...
'a'-->is used to add the txt info file at last index, if file dose nit exist...
'w'-->is used to add the txtx into file but it will override of all txtx
inside file. if the file does not exist it will create with that name...
'x'-->used to create the file. but will throug error if we are used 'r' mood to
create...

method
------
write()
read()
-->this method can read entire file chunk where we can

readline()
readlines()

readline()
----------
-->can read only one at a time in a file...
readlines()
-----------
-->it will read entire file and gives in a list whare each line is each index
in the list


'''
any_ = open('demo.txt','r')
print(any_.readlines())
any_.close()


   1`````````````````2ÁWA1w2qZSWzd3xdefcgrfvh56b

































