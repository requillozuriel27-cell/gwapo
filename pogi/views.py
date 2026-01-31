from django.shortcuts import render

# Creafrom django.shortcuts import render

# This function name must match what you wrote in urls.py
def home(request):
    return render(request, 'home.html')
