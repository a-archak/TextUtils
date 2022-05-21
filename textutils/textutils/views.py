# I created this file - Archak 
from django.http import HttpResponse
from django.shortcuts import render
    
#BASIC DJANGO PRACTICE CODES
    # def index(request):
    #     return HttpResponse('''
    #     <h1>Hi I'm Archak.</h1>
    #     <a href="https://www.facebook.com/"> Go To Facebook </a>
    #     ''')

    # def about(request):
    #     return HttpResponse("I am a student.")

    # #to display contents of file1.txt in browser
    # def fileOpen(request):
    #         f=open("file1.txt", "r")
    #         file_content=f.read()
    #         f.close()
    #         return HttpResponse(file_content, content_type="text/plain")


#STARTING CODE FOR TEXTUTILS PROJECT
def index(request):
    return HttpResponse("Home")

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
