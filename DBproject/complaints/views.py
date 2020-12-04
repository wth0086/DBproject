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
