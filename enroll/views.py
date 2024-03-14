from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView
# Create your views here.


# This is code for show student data 

class AddTemplateView(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu':stud, 'form':fm}
        return context



# def add_student(request):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             password = fm.cleaned_data['password']
#             reg = User(name = name, email=email, password=password)
#             reg.save()
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()
#     stud = User.objects.all()
#     return render(request, 'enroll/addandshow.html', context={'form':fm, 'stu':stud})


# Update / Edit Record of student 

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm  = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
         pi.save()
    else:
        pi = User.objects.get(pk=id)
        fm  = StudentRegistration( instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})













# This is code of delete data from table 

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')







