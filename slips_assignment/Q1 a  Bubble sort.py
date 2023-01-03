def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i]=list[i+1]
                list[i+1] = temp

list = [56,11,63,97,17,68,15,61,40]
bubbleSort(list)
print(list)