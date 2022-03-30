from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EnterHTML
# Create your views here.

#def converted(request):
    #return render(request, 'converted.html')


def index(request):
    #return HttpResponse("Hello, world. You're at the HTML gen index")

    if request.method == "POST":
        form = EnterHTML(request.POST)
        
        if form.is_valid():
            n = form.cleaned_data["enterHTML"]
            #print(n)
           # x = n.replace("\n", " NL ")
            #print(x)
            convertedString =  "<p>{str}</p>".format(str=n)
            print(convertedString)
            return render(request, 'generator.html', {"form":form, "convertedString":convertedString})
            #return HttpResponse(convertedString)



        
            
    else: 
        form = EnterHTML()
    return render(request, 'generator.html', {"form":form})
