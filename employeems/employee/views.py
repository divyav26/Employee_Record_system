from datetime import datetime

from django.contrib.auth import login, logout,authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def add_emp(request):
    if request.method == "POST":
        first_name  = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus =int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name,salary=salary,bonus=bonus, dept_id=dept,role_id =role, phone=phone, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse("<body bgcolor ='pink'><center><h1>Employee Added Successfully</h1></center></body>")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("error")



def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request,'all_emp.html', context)

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_removed = Employee.objects.get(id=emp_id)
            emp_to_removed.delete()
            return HttpResponse("<body bgcolor ='pink'><center><h1>Employee Data Remove Successfully</h1></center></body>")
        except:
            return HttpResponse("Error")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'remove_emp.html',context)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps =  Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if dept:
            emps = emps.filter(dept__name = dept)

        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps':emps
        }
        return render(request,'all_emp.html', context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Error")


    return render(request,'filter_emp.html')


