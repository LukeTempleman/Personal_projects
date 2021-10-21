def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):

            if list[j] > list[j +1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j+1] = temp

    return list




arraylist = [1,3,2,9,6,4]

print(bubblesort(arraylist))