from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method == "POST":
        result = request.POST.get('result', '')
        
        return render(request, 'index.html', {'result':result})
    
    return render(request, 'index.html')