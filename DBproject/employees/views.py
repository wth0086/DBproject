from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from employees.models import Employee
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login


# Create your views here.
# a
def login_page(request):
    return render(request, 'employees/login.html')

def loginEmployee(request):
    if request.method == "POST":
        user = AuthenticationForm(request, request.POST)
        if user.is_valid:
            login(request, user.get_user())
            return HttpResponseRedirect(reverse('employees:emAll'))
        else:
            return render(request, 'employees/login.html', {'error': 'ID or PW is incorrect'})
    else:
        render(request, 'employees/login.html')


def regEmployee(request):
    return render(request, 'employees/registerEmployee.html')

def regConEmployee(request):
    ID = request.POST['ID']
    PW = request.POST['PW']
    name = request.POST['name']
    gender = request.POST['gender']
    work_type = request.POST['work_type']
    birthdate = request.POST['birthdate']
    address = request.POST['address']
    phone_number = request.POST['phone_number']

    qs = Employee(e_ID=ID, e_PW=PW, e_name=name, e_gender=gender, e_work_type =work_type, 
    e_birthdate=birthdate, e_address=address, e_phone_number=phone_number)

    if qs.is_valid():
        qs.save()
        return HttpResponseRedirect(reverse('employees:login'))
    else:
        return render(request, 'employees/registerEmployee.html', {'error': 'There is a blank field'})

def readEmployeeAll(request):
    qs = Employee.objects.all()
    context = {'Employee_list': qs}
    return render(request, 'employees/readEmployees.html', context)

def Employeeinfo(request, ID):
    qs = Employee.objects.get(e_ID = ID)
    context = {'Employee_info': qs}
    return render(request, 'employees/Information.html', context)

def readEmployeeOne(request, ID):
    qs = Employee.objects.get(e_ID = ID)
    context = {'Employee_info': qs}
    return render(request, 'employees/Modify.html', context)

def modConEmployee(request):
    ID = request.POST['ID']
    name = request.POST['name']
    gender = request.POST['gender']
    work_type = request.POST['work_type']
    birthdate = request.POST['birthdate']
    address = request.POST['address']
    phone_number = request.POST['phone_number']

    e_qs = Employee.objects.get(e_ID=ID)

    e_qs.e_name = name
    e_qs.e_gender = gender
    e_qs.e_work_type = work_type
    e_qs.e_birthdate = birthdate
    e_qs.e_address = address
    e_qs.e_phone_number = phone_number

    e_qs.save()

    return HttpResponseRedirect(reverse('employees:emAll'))

def delConEmployee(request, ID):
    qs = Employee.objects.get(e_ID = ID)
    qs.delete()

    return HttpResponseRedirect(reverse('employees:emAll'))