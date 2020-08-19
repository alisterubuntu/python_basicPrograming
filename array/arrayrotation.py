import numpy as np

def function_leftrotate(arr,spliter):
    counter = 0
    #newArr = np.empty([10])
    newArr = []
    newArr2 = []
    for i in range(len(arr)-spliter,len(arr)):
        newArr.append(arr[i])
        counter =+1
    for i in range(len(arr) - spliter):
        newArr2.append(arr[i])
        counter = +1

    newlist3 = newArr + newArr2
    print(newlist3)
    

arr = [1, 2, 3, 4, 5, 6, 7]
function_leftrotate(arr,2)


