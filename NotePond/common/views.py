from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def noteSearch(request):
    return render(request, 'noteSearch.html')

def noteView(request):
    return render(request, 'noteView.html')

def noteUpload(request):
    return render(request, 'noteUpload.html')