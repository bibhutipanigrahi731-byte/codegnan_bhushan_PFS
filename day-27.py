#day 26
'''
matplotlib
----------
--> this is a library in python for data visualization, allowing user to create
a variety of plots...

basic stucture of matplotlib
----------------------------
-->figure
-->axis
-->guird
-->length


import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25,15,90]
plt.bar(sales,values)
plt.xlable('Cae Module')
plt.ylable('values')
plt.tital('BMW sales')
plt.show()


import matplotlib.pyplot as plt
overs = [1,2,3,4,5]
score = [10,20,30,40,50]
plt.plot(overs,score)

plt.ylabel('score')
plt.xlabel('overs')
plt.title('scorecard')
plt.show()


import matplotlib.pyplot as plt
subjects = ['python','java','c']
students = [37,7,25]
plt.pie(students,labels=subjects,autopct='%1.if%%')
plt.legend(subjects)
plt.title('student in scorce')
plt.show()


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,20,35,24]

plt.scatter(x,y)
plt.title('scatter plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()


import matplotlib.pyplot as plt
y = [10,20,30,40,50]
plt.hist(y)
plt.title('histogram plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

'''
import matplotlib.pyplot as plt
sales = [200,300,400,500,600,700,800,900]
plt.hist(sales)
plt.title('histogram plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()












