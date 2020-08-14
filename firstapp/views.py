#from django.http import HttpResponse
#from django.template import loader
 
from django.shortcuts import render
from datetime import datetime 
 
def index(request):
    #template = loader.get_template('firstapp/index.html')
    now = datetime.now()
    context = {
       'current_date' : now
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'firstapp/index.html', context)
 
def select(request):
    context={'number' : 4}
    return render(request, 'firstapp/select.html', context)
 
def result(request):
    context={'numbers' : [1,2,3,4,5,6]}
    return render(request, 'firstapp/result.html', context)