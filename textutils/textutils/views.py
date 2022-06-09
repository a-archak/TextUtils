# I created this file - Archak 
from email.policy import default
from string import punctuation
from sys import displayhook
from django.http import HttpResponse
from django.shortcuts import render
    
#STARTING CODE FOR TEXTUTILS PROJECT
def index(request):
    return render(request, "index.html")

def analyze(request):
    #getting text from text field and printing it in Remove Punctuation Page
    displayText=request.POST.get('text', 'default')
    #getting checkbox input
    removePunc=request.POST.get('removePunc', 'off')
    uppercase=request.POST.get('uppercase', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charactercounter=request.POST.get('charactercounter', 'off')
    # declaring required variables
    results = ""
    purpose = ""

    #removing punctuations in user entered text
    if (removePunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        #Checking if any characters is a punctuation character
        for char in displayText:
            if char not in punctuations:
                analyzed = analyzed + char
        # modifying parameters
        purpose += " | Remove Punctuation | "
        displayText = analyzed

    # Changing user entered characters into uppercase
    if (uppercase=="on"):
        analyzed = ""
        # iterating through every letters, capitalizing them and merging them
        for char in displayText:
            analyzed = analyzed + char.upper()
        # modifying parameters
        purpose += " | Upper Case | "
        displayText = analyzed

    # Removing new line in given text
    if (newlineremover=="on"):
        analyzed = ""
        # iterating through every letters, removing new lines and merging them
        for char in displayText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        # modifying parameters
        purpose += " | New Line Removed | "
        displayText = analyzed

    # Removing extra spaces from given texts
    if (extraspaceremover=="on"):
        analyzed = ""
        # iterating through every characters, removing extra spaces and merging them
        for index, char in enumerate(displayText):
            if not(displayText[index] == " " and displayText[index+1] == " "):
                analyzed = analyzed + char
        # modifying parameters
        purpose += " | Extra Space Removed | "   
        displayText = analyzed
        
    # Counting Number of characters in given text
    if (charactercounter=="on"):
        count = 0
        # iterating through every characters, removing extra spaces and merging them
        for char in displayText:
            count = count +1
        # modifying parameters
        purpose += " | Character Counts | "
        analyzed += ". And the number of characters are " + str(count)

    # to show results in analyzed.html    
    if removePunc=="on" or uppercase=="on" or charactercounter=="on" or newlineremover=="on" or extraspaceremover=="on":
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    # results to show if no punctuation is choosed
    else:
        return HttpResponse('Error')
    #rendering outputs with parameters in analyze.html

# to render aboutus page
def aboutus(request):
    return render(request, "aboutus.html")

# to render contactus page
def contactus(request):
    return render(request, "contact.html")