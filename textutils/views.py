#I have created this file - Amey

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Check the checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert to upper case', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!= "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcount == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
            if char!=" ":
             count+=1
        analyzed = analyzed + f"the character count of {djtext} is {count}"
        params = {'purpose': 'Count the characters', 'analyzed_text': analyzed}
        #djtext = analyzed


    if (removepunc =="off" and fullcaps == "off" and newlineremover=="off" and extraspaceremover=="off" and charcount=="off") :
        return HttpResponse("please select an operation")

    return render(request, 'analyze.html', params)


def about_us(request):
    return render(request,'about.html')

def  contact_us(request):
    return render(request,'contact.html')
