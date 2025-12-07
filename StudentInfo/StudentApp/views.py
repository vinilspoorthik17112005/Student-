from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, welcome to the Student Info App!")
def student(request):
    # Logic to fetch and display student details
    return render(request,'student.html')
def landing(request):
    return render(request, 'landing.html')
def contact(request):
    return render(request, 'contact.html')
    return render(request,'landing.html')
def courses(request):
    return render(request,'courses.html')

# Create your views here.
