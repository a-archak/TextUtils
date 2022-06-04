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
    displayText=request.GET.get('text', 'default')
    #getting checkbox input
    removePunc=request.GET.get('removePunc', 'off')
    uppercase=request.GET.get('uppercase', 'off')
    newlineremover=request.GET.get('newlineremover', 'off')
    extraspaceremover=request.GET.get('extraspaceremover', 'off')
    charactercounter=request.GET.get('charactercounter', 'off')

    #removing punctuations in user entered text
    if (removePunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        #Checking if any characters is a punctuation character
        for char in displayText:
            if char not in punctuations:
                analyzed = analyzed + char
        #storing parameters in Json form
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # rendering results in template
        return render(request, 'analyze.html', params)

    # Changing user entered characters into uppercase
    elif (uppercase=="on"):
        analyzed = ""
        # iterating through every letters, capitalizing them and merging them
        for char in displayText:
            analyzed = analyzed + char.upper()
        # storin results in Json form
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        # rendering results in template
        return render(request, 'analyze.html', params)

    # Removing new line in given text
    elif (newlineremover=="on"):
        analyzed = ""
        # iterating through every letters, removing new lines and merging them
        for char in displayText:
            if char != "\n":
                analyzed = analyzed + char
        # storin results in Json form
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        # rendering results in template
        return render(request, 'analyze.html', params)

    # Removing extra spaces from given texts
    elif (extraspaceremover=="on"):
        analyzed = ""
        # iterating through every characters, removing extra spaces and merging them
        for index, char in enumerate(displayText):
            if not(displayText[index] == " " and displayText[index+1] == " "):
                analyzed = analyzed + char
        # storin results in Json form
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        # rendering results in template
        return render(request, 'analyze.html', params)

    
    # Counting Number of characters in given text
    elif (charactercounter=="on"):
        count = 0
        # iterating through every characters, removing extra spaces and merging them
        for char in displayText:
            count = count +1
        # storin results in Json form
        params = {'purpose': 'Character Counted', 'analyzed_text': count}
        # rendering results in template
        return render(request, 'analyze.html', params)

    # results to show if no punctuation is choosed
    else:
        return HttpResponse('Error')