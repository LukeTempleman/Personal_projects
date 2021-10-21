
def singleValue(array,input):
    for i in range(len(array)):
        array[i] = input

    print(array)
    return array


def incrementOrDecrement(array,boolean):
    for i in range(len(array)-1,0,-1):

        for j in range(i):

            if array[j] > array[j+1] and boolean == True:

                temporary = array[j]
                array[j] = array[j+1]
                array[j+1] = temporary

            elif array[j] < array[j+1] and boolean == False:

                temporary = array[j+1]
                array[j + 1] = array[j]
                array[j] = temporary

    print(array)
    return array


def interface():
    array = [1,4,3,6,4,3,5,6,3]

    while True:
        print("1.)Fill array with given value \n 2.)Sort array in ascending or descending order")
        userinput = input("Please enter method number: ")

        if userinput == "1":
            valueOfArray = input("please enter value to fill array with: ")
            singleValue(array, valueOfArray)

        elif userinput == "2":
            boolean = input("should the array be sorted in asc or dsc?: ")

            if boolean == "asc":
                incrementOrDecrement(array, True)

            else:
                incrementOrDecrement(array, False)


interface()







