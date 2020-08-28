from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
   #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})
def contact_view(request,*args, **kwargs):
    #return  HttpResponse("<h1>Contact page</h1>")
    return render(request,"contact.html",{})
def about_view(request,*args,**kwargs):
    #return HttpResponse("<h1>About</h1>")
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "this is true":True,
        "my_list": [123,4343,32323,"sdsdbu"]
    }

    return render(request, "about.html",my_context)
