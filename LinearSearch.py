import numpy as np
a = np.array([4, 1,2 ,3])
num = int(input("Enter the number to be searched : "))
for i in range(len(a)):
    if(a[i] == num):
        print("Number found")
        break
if(a[i] != num):
    print("Number not found")


