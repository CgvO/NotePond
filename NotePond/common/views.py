from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def noteSearch(request):
    return render(request, 'base.html')

def noteView(request):
    return render(request, 'base.html')

def noteUpload(request):
    return render(request, 'base.html')