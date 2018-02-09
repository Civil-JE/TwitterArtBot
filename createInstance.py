class CreateRedditInstance:
    #Insert your own information here
    client_id = "" 
    client_secret = ""
    user_agent = ""
    username = ""
    password = ""

    def setRedditInfo(self):
        credentialsFile = "Credentials.txt" #Change if your file is named different
        openedFile = open(credentialsFile,"r")
        credentials = openedFile.readlines()

        #Had to add .strip to remove invisible whitespaces/leading characters
        self.client_id = credentials[0].strip()
        self.client_secret = credentials[1].strip()
        self.user_agent = credentials[2].strip()
        self.username = credentials[3].strip()
        self.password = credentials[4].strip()
