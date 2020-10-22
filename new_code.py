import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

#Code by - Aditya Agrawal

dataframe = pd.read_csv("Main.csv")
dataframe.fillna(0)
#print(dataframe.head(36))
dataframe1 = pd.read_csv("Main.csv") 

df = dataframe.sort_values("Number of Persons Killed from accidents of Two-Wheelers - 2012")

new_list = df["Number of Persons Killed from accidents of Two-Wheelers - 2012"].tolist()
new_list1 = df["States/UTs"].tolist()

print(new_list)
print(new_list1)

print(len(new_list))
print(len(new_list1))

a1=[]
b1=[]
a2=[]
b2=[]
a3=[]
b3=[]
a4=[]
b4=[]

for i in range(0,10):
    a1.append(new_list[i])
for i in range(0,10):
    b1.append(new_list1[i])

print(a1)    
print(b1)

for i in range(10,20):
    a2.append(new_list[i])
for i in range(10,20):
    b2.append(new_list1[i])

print(a2)    
print(b2)

for i in range(20,30):
    a3.append(new_list[i])
for i in range(20,30):
    b3.append(new_list1[i])

print(a3)    
print(b3)

for i in range(30,37):
    a4.append(new_list[i])
for i in range(30,37):
    b4.append(new_list1[i])
    
plt.bar(b1,a1,align='center',alpha=1)
plt.title("Year 2012 Plot - 1st ")
plt.show()

plt.bar(b2,a2,align='center',alpha=1)
plt.title("Year 2012 Plot - 2nd ")
plt.show()

plt.bar(b3,a3,align='center',alpha=1)
plt.title("Year 2012 Plot - 3rd ")
plt.show()

plt.bar(b4,a4,align='center',alpha=1)
plt.title("Year 2012 Plot - 4th ")
plt.show()


dafr = dataframe1.sort_values("Two-Wheelers - Number of Persons-Killed - 2014")

new_list14 = dafr["Two-Wheelers - Number of Persons-Killed - 2014"].tolist()
new_list114 = dafr["States/UTs"].tolist()

print(new_list14)
print(new_list114)

print(len(new_list14))
print(len(new_list114))

a5=[]
b5=[]
a6=[]
b6=[]
a7=[]
b7=[]
a8=[]
b8=[]

for i in range(0,10):
    a5.append(new_list14[i])
for i in range(0,10):
    b5.append(new_list114[i])

print(a5)    
print(b5)

for i in range(10,20):
    a6.append(new_list14[i])
for i in range(10,20):
    b6.append(new_list114[i])

print(a6)    
print(b6)

for i in range(20,30):
    a7.append(new_list14[i])
for i in range(20,30):
    b7.append(new_list114[i])

print(a7)    
print(b7)

for i in range(30,37):
    a8.append(new_list14[i])
for i in range(30,37):
    b8.append(new_list114[i])
    
plt.bar(b5,a5,align='center',alpha=1)
plt.title("Year 2014 Plot - 1st ")
plt.show()

plt.bar(b6,a6,align='center',alpha=1)
plt.title("Year 2014 Plot - 2nd ")
plt.show()

plt.bar(b7,a7,align='center',alpha=1)
plt.title("Year 2014 Plot - 3rd ")
plt.show()

plt.bar(b8,a8,align='center',alpha=1)
plt.title("Year 2014 Plot - 4th ")
plt.show()


