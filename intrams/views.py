from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   return render(request, 'accounts/hompe page.html')

def teams(request):
   return render(request, 'accounts/team.html')

def courses(request):
   return render(request, 'accounts/courses.html')

def student(request):
   return render(request, 'accounts/student.html')
