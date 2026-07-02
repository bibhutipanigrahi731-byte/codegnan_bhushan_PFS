#day-23
'''
regular expression (regex)
-------------------------
-->regex is a square of char that from a searchimg pattern....
-->this can be squence to check if a string contain the specified search pattern

-->python has a built-in packeage called 're' which cannbe used to work with
regex...

functions in re
---------------
1.fimdall
2.search
3.fullmatch

metachar
-------
[]-->a-z,A-Z,0-9 and any specified squence...
. -->hearbeach dot is one char
^ -->this look for the, string is starting with spacified aquence or not...
$ -->this look for the, string is ending with spacified squence or mot...
* -->zero or more
? -->zero or one
+ -->one or more
{}-->

spacial squence
---------------
\S -->no space
\s -->only space
\D -->None-disit
\d -->only-digits
\w -->matchs any word char (lettars, disits, underscore)
\W -->

import re
any_ = "python is a foundational, general-purpose programming langugae created by dennis"
print(re.findall('^python is',any_))



import re
any_ = "python is a foundational"
print(re.findall('foundational$',any_))



import re
any_ = "python is a foundational"
print(re.findall('p.*thon',any_))


import re
any_ = "python is a 345 @foundational"
print(re.findall('\w',any_))

'''
import re
mobile_ = input("enter 10 disit india mobile number")
how = re.fullmatch('[6-9][0-9]{9}',mobile_)
if how:
    print(f"{mobile_} this is india number")
else:
    print(f"{mobile_} this is not india number")







