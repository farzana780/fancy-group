from django.shortcuts import render, redirect, get_object_or_404
from .models import Job_Apply
from .models import Team, Circular, Departments, Contact
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        emailaddress = request.POST['emailaddress']
        subject = request.POST['sendersubject']
        message = request.POST['sendermessage']

        x = Contact.objects.create(full_name=full_name, emailaddress=emailaddress, subject=subject, message=message)
        x.save()
        return redirect('/')
    else:
        return render(request, 'others/contact.html')


def about(request):
    team = Team.objects.all()
    return render(request, 'others/about.html', {'team': team})


def career(request, dept_slug=None):
    dept = None
    circular = Circular.objects.all()
    department = Departments.objects.all()
    if dept_slug:
        dept = get_object_or_404(Departments, slug=dept_slug)
        circular = circular.filter(department_name=dept)
    return render(request, 'others/career.html', {'circular': circular, 'department': department, 'dept': dept})


def job_details(request):
    job = get_object_or_404(Circular, slug=request.GET.get('id'))
    return render(request, 'others/job_details.html', {'job': job})


def job_apply(request):
    job = get_object_or_404(Circular, slug=request.GET.get('id'))
    if request.method == 'POST':
        full_name = request.POST['full_name']
        emailaddress = request.POST['emailaddress']
        phone_number = request.POST['phone_number']
        file = request.POST['file']
        x = Job_Apply.objects.create(full_name=full_name, email_address=emailaddress, phone_number=phone_number,
                                     file=file, job_title=job)
        x.save()
        messages.success(request, 'Application is submitted successfully')
        return redirect('others:career')

    else:
        return render(request, 'others/job_apply_form.html', {'job': job})

