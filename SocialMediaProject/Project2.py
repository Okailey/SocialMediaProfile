#PROJECT 2

class Profile:
    

    def __init__(self, fullname, dateOfBirth, username, bio):
        self.numFollowersAfterAccCreated = 0
        self.fullname = fullname
        self.dateOfBirth= dateOfBirth
        self.username= username
        self.bio= bio
        
        

#the string function
    def __str__( self ):
        form = "Full name: " + self.fullname + ",  Age: " + self.dateOfBirth + ",  Profile username: " + self.username +  ",  Bio: " + self.bio + ",  Number of Followers: " +  str(self.numFollowersAfterAccCreated)
        return form
    
    #the getter for fullName
    def getFullName(self):
        return self.fullname
    
    #the getter for age
    def getAge(self):
        return self.dateOfBirth
    
    #the getter for username
    def getUsername(self):
        return self.username
    
    #the getter for bio
    def getBio(self):
        return self.bio
    
    #the getter for NumFollowersAfterCreated
    def getNumFollowersAfterAccCreated(self):
        return self.numFollowersAfterAccCreated
    

    #the setter for NumFollowersAfterCreated
    def setNumFollowers(self, newNumFollowersAfterAccCreated):
        self.numFollowersAfterAccCreated = newNumFollowersAfterAccCreated
    


# Function askAcctQuestionnaire asks the user the questions provided as an argument (questionList) and returns their answers as a list
def askAcctQuestionnaire( questionList):
    
    #the empty list where the response to the questions asked will be stored
    profileInstanceList = []
   
    # For each question provided in the list of questions
    for question in questionList:
        # Ask the user for their response to that question
        response = input(question)
        # Add their response to the profileInstance list
        profileInstanceList.append(response)

    # Return the list of answers the user provided
    return profileInstanceList






def main():
    
    questionList = ["What is your full name? " , "What is your date of birth?(in the form MM/DD/YYYY) ", "What should your username be? ", "What do you want in your bio? "]
    theInstances = []

    #  a for loop to iterate through the questionList and to ask the questions 3 times
    for thesequestions in range(3):
        ansForQuestions = askAcctQuestionnaire(questionList)
        #append the user's input to theInstances list
        theInstances.append(Profile(ansForQuestions[0],  ansForQuestions[1],  ansForQuestions[2],  ansForQuestions[3]))
    
    #printing the user's input using the for loop
    for answers in theInstances:
        print (answers)

    #changes the property numFollwers default value to 200 for for the first person, 
    # initially the person had 0 followers and now the person will have 200.
    theInstances[0].setNumFollowers(200)
    print(theInstances[0])

if __name__ == "__main__":
    main()