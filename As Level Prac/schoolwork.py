def AddNewScores():
    dateOfScores = input("Please enter the date of the scores ") #4 DIGIT STRING

    while True:
        memberShipNumber = input("Please enter membership number ") #six-digit numeric String

        if memberShipNumber == "":
            break


        while True:
             score = input("Please enter score ") #two digit String

             if score >= "50" and score <= "99":
                 textString = memberShipNumber+dateOfScores+score  # A String containing all the data 
                 textfile = open("ScoreDetails.txt","w")
                 textfile.write(textString)
                 textfile.close()
                 break
                 


               

        




AddNewScores()