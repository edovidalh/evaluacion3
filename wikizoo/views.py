from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'wikizoo/Main.html')

def animal(request):
    return render(request, 'wikizoo/Animal.html')