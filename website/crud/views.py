from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
def list_employee(request):
    employee_set = Employee.objects.all()
    return render(request, 'index.html', {'employees': employee_set})


def add_form(request):
    """to add employee"""

    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_employee')  # URL redirection

    return render(request, 'addemp.html', {"form": form})


def edit_employee(request, pk, template_name='edit.html'):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('list_employee')

    return render(request, template_name, {'form': form})


def delete_employee(request, pk, template_name='confirm_delete.html'):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('list_employee')

    return render(request, template_name, {'object': employee})


def employee_details(requests, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(requests, 'details.html', {'employee': employee})
