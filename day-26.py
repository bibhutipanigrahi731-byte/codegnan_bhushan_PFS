#day-26
'''
data analysis
-------------
--> this is process of inspecting, cleaning, transforming, and modeling data to discover useful insights...

type of DA
----------

1.descriptive  analysis
------------------------
-->summarizing data

2.dignostic  analysis
---------------------
-->understanding causes

3.predictive  analysis
-----------------------
-->forecasting future outcomes

4.prescriptive  analysis
------------------------
-->syggesting actins based on data


why DA
------
-->to improve decision
-->detects trends & pattrens
-->


numpy (numerical python)
-----
-->this python library for numerical comuting. it provides support for
multi-dimensional arrays, and linear algebra operattions, making it essent
for data  analysis....

using numpy in DA
------------------
-->improved performance
-->simplifiles complex operations
-->easy data munipulation...



import numpy as np
arr_1 = np.array([[1,2,3,4],[4,6,8,5],[3,6,9,7]])
print(arr_1)



import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshaped(4, 3)
print(reshaped)



import numpy as np
arr_1 = np.array([[1,2],[4,5]])
arr_2 =  np.array([[6,7],[8,9]])
        
print(np.dot(arr_1, arr_2))


data
import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)

copy_dee = arr_1.copy()
arr_1[1] = 200
print(copy_dee)
print(arr_1)

pandas
------
-->the pandas is a powerful datab manipilation and analysis libarary...
-->where it provides data stucture like series and dataframe for efficent
data handaling

methods series
--------------
mean()
sum()
max()
min()
apply()
map()


dataframe
----------


import pandas as pd
any_ = pd.series([2999,15999,56999,7999,19999],index=['earbuds','smartphone','lap','watch','footware'])
print(any_)


'''
import pandas as pd
data = {
    'prodect':['earbuds','smartphone','lap','watch','footware'],
    'brand':['noice','oneplus','HP','bolt','nike'],
    'price':['1599','15999','53999','1999','3999'],
    'stock':[50,15,25,40,70]
    }
dip = pd.DataFrame(data)
print(dip)








