from django.shortcuts import render, redirect

#Check User Input
def userSearch(response, data):
        
        #Searches with a Hidden  Directory
        if data == "dino":
            return render(response, "main/result_dino.html")

        elif data == "pandaz":
            return render(response, "main/result_pandaz.html")

        elif data == "TyperzXtremeChallenge":
            return render(response, "main/result_TyperzXtremeChallenge.html")

        elif data == "Show me the flag please sir.":
            return render(response, "main/result_flagPleaseSir.html")

        #Searches with a Visible Directory (Redirect to auth.py)
        elif data == "CYBER.ORG Staff":
            return redirect("/cyberStaff")
            
        elif data == "RARC 2021":
            return redirect("/RARC2021")

        #Search Not Found
        else:
            return render(response, "main/result_noneFound.html")
    

#Home Path
def index(response):
    if response.method == "POST":
        
        #Konami Code False by default
        The_Recording_Is_Satisfied = False
    
        #Gets the user's Search Input
        userInput = response.POST['userInput']

        #Gets the user's Keypresses to check Konami Code
        userRecording = response.POST.get('userRecording', False)

        #Checks if the user is focused on the search bar
        searchFocus = response.POST.get('searchFocus', False)
        
        #If the search bar unfocused
        if searchFocus == "false":
            print(userRecording)
        #Konami Code was input by user 
            if userRecording == "ArrowUp,ArrowUp,ArrowDown,ArrowDown,ArrowLeft,ArrowRight,ArrowLeft,ArrowRight,b,a,Enter":
                print("Konami Code Entered")
                The_Recording_Is_Satisfied = True
            return render(response, "main/index.html", {"The_Recording_Is_Satisfied": The_Recording_Is_Satisfied})

        #Check User Input
        return userSearch(response, userInput)
    
    return render(response, "main/index.html") 

#Visible Goober Paths
def cyberStaff(response):
    if response.method == "POST":

        #Gets the user's Search Input
        userInput = response.POST['userInput']

        #Check User Searches
        return userSearch(response, userInput)

    return render(response, "main/result_cyberStaff.html")

def RARC2021(response):
    if response.method == "POST":

        #Gets the user's Search Input
        userInput = response.POST['userInput']

        #Check User Searches
        return userSearch(response, userInput)

    return render(response, "main/result_RARC2021.html")
