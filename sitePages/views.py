from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'sitePages/about.html')
