start = 100
end = 200

for i in range(start,end):
    flag = False
    halfDiv = int(i/2)
    for j in range(2,halfDiv):
        if i % j == 0 :
            flag = True
            break
    if flag == False:
        print(i)
