from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm


def list_emp(request):
    return render(request, "employee_register/list_emp.html")


def form_emp(request):
    form = EmployeeForm()
    return render(request, "employee_register/form_emp.html",{'form':form})


def delete_emp(request):
    return
