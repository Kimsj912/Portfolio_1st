from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dev(request):
    return render(request, 'myppl_dev.html')

def proj(request):
    return render(request, 'myppl_proj.html')

def asset(request):
    return render(request, 'myppl_asset.html')    
