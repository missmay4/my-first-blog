from django.shortcuts import render

# Create your views here.
def main_web(request):
    return render(request, 'web/main.html')
def aboutme(request):
    return render(request, 'web/about_me.html')
