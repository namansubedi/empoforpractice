from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def explore(request):
    return render(request, 'explore.html')

def show(request):
    val1 = request.POST["emails"]
    val2 = request.POST["pws"]
    return render(request, 'show.html', {'v1': val1})
