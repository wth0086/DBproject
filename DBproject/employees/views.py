from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from employees.models import Employee
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login


# Create your views here.
# a
def login_page(request):
    return render(request, 'employees/login.html')

def loginEmployee(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'employees/login.html')

    elif request.method == "POST":
        login_ID = request.POST.get('ID', None)
        login_PW = request.POST.get('PW', None)

        if not(login_ID and login_PW):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요"
        else:
            myuser = Employee.objects.get(e_ID=login_ID)
            if check_password(login_PW, myuser.e_PW):
                request.session['user'] = myuser.e_ID
                return HttpResponseRedirect(reverse('employees:emAll'))
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'employees/login.html', response_data)


def regEmployee(request):
    return render(request, 'employees/registerEmployee.html')

def regConEmployee(request):
    ID = request.POST['ID']
    PW = request.POST['PW1']
    re_PW = request.POST['PW2']
    name = request.POST['name']
    gender = request.POST['gender']
    work_type = request.POST['work_type']
    birthdate = request.POST['birthdate']
    address = request.POST['address']
    phone_number = request.POST['phone_number']
    res_data = {}

    if not (ID and PW and re_PW and name and gender and work_type and address and phone_number):
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'employees/registerEmployee.html', res_data)
    if PW != re_PW:
        res_data['error'] = '비밀번호가 다릅니다.'
        return render(request, 'employees/registerEmployee.html', res_data)
    else:
        qs = Employee(e_ID=ID, e_PW=make_password(PW), e_name=name, e_gender=gender, e_work_type =work_type, 
        e_birthdate=birthdate, e_address=address, e_phone_number=phone_number)
        qs.save()
        return HttpResponseRedirect(reverse('employees:login'))

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