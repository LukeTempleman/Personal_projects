def linearSearch(list, num):
    found = False;
    for i in range(len(list)):
        if list[i] == num:
            found = True
            print("Found number at index: "+ str(i))

    if found == False:
        print("could not find number in list")


list = [10,45,64,8,432,45]

linearSearch(list,100)