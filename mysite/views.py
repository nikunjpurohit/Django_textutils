from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'nikunj','place':'jaipur'}
    
    return render(request,'index.html',params)
    
    #return HttpResponse('''<h1>hello Yo</h1> <a href='https://www.codewithharry.com/blogpost/django-cheatsheet/'> about</a>''') 
def analyze(request):
    djtext= request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    print(fullcaps)
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    if removepunc == "on":
        s=0
        for i in djtext:
            if i ==" ":
                continue
            else:
                s=s+1
        print("The number of characters in this string is:",s)
        for char in djtext:
            if char not in punctuations:
                analyzed =analyzed+char
        params={'purpose':'Remvoed Punctuation','analyzed_text':analyzed,'count':s}
        return render(request,'analyze.html',params)
    elif fullcaps =="on":
        
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Remvoed Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
        
    else:
        return HttpResponse('Error')
    

def about(request):
    return HttpResponse("Tell me about Yo") 

