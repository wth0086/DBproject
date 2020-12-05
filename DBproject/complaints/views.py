from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Complain, Employee
from .forms import ComplainForm


def complaints(request):
    complains = Complain.objects.all()
    return render(request, 'complaints/complaints.html', {'complain_list': complains})


def complain_text(request):

    if request.method == 'POST':
        form = ComplainForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('complaints')
    else:
        form = ComplainForm()

    return render(request, 'complaints/complain_text.html', {'form': form})

def checkstate(request):
    if request.method == "POST":
        worktype = request.POST.get('worktype', None)
        qs = Employee.objects.filter(e_work_type = worktype)
        context = {'By_Worktype': qs}
        return render(request, 'complaints/checkstate.html', context)

def savestate(request, complain_number):
    if request.method == "POST":
        qs = Complain.objects.get(complain_number = complain_number)
        qs_e = Employee.objects.get(e_ID = qs.employee_ID)

        complain_type = qs.complain_type.complain_type
        room_number = qs.room_number.room_number
        problem_type = qs.problem_type
        str = complain_type + '_' + room_number + '_' + problem_type

        qs.complain_code = str
        qs.save()

        if (qs_e.complain_code == None):
            qs_e.complain_code = str
            qs_e.save()
        else:
            qs_e.complain_code += " / " + str
            qs_e.save()


        

        return HttpResponseRedirect(reverse('complaints'))

