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
    displayPunc=request.GET.get('removePunc', 'off')
    #removing punctuations in user entered text
    if displayPunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in displayText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
    return HttpResponse("Remove Punctuation <a href='/'> Back</a>")