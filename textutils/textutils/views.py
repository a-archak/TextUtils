# I created this file - Archak 
from django.http import HttpResponse
from django.shortcuts import render
    
#STARTING CODE FOR TEXTUTILS PROJECT
def index(request):
    params = {'name':'Archak', 'place':'Hetauda'}
    return render(request, "index.html", params)

def removePunc(request):
    return HttpResponse("Remove Punctuation <a href='/'> Back</a>")

def capFirst(request):
    return HttpResponse("Capitalize First <a href='/'> Back</a>")

def newLineRemove(request):
    return HttpResponse("New Line Remover <a href='/'> Back</a>")

def spaceRemove(request):
    return HttpResponse("Space Remove <a href='/'> Back</a>")

def charCount(request):
    return HttpResponse("Character Count <a href='/'> Back</a>")
