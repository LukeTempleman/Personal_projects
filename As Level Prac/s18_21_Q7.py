def ProcessMarks(Mark):
    average = 0
    highestMark = 0
    for i in range(len(Mark)):
        if highestMark < Mark[i]:
            highestMark = Mark[i]

        average = average + Mark[i]

    average = average / len(Mark)

    outPutMessage = "The average mark is " + str(average) + " and the highest mark is " + str(highestMark)

    return(outPutMessage)

Mark = [10,20,10,40,40,50]
print(ProcessMarks(Mark))