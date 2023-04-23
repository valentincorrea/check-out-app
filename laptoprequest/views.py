from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models.aggregates import Count
from django.db.models import F, Q
from .models import Computer, Request, NewUser, AbstractUser
from .forms import RequestForm, ApproveForm
from django.contrib import messages
# Send emails
from django.core.mail import send_mail
import asyncore
import asyncio
from django.db.models import Q



# Create your views here.
def home(request):
    standart_count = Computer.objects.filter(status='Available').filter(computer_classification='Standard').count()
    performance_count = Computer.objects.filter(status='Available').filter(computer_classification='Performance').count()
    return render(request, 'index.html', {'standart_count': standart_count, 'performance_count':performance_count, 'navbar':'home'})

def computers(request):
    #Pagination
    pagination = Paginator(Computer.objects.filter(status='Available').all().order_by('id'), 20)
    page = request.GET.get('page')
    pages = pagination.get_page(page)
    return render(request, 'computers.html', {'pages': pages, 'navbar':'computers'})


def computer_detail(request, id):
        computer_datail = Computer.objects.get(pk=id)
        return render(request, 'computer_details.html', {'computer_datail':computer_datail})

def request_form(request):
    url = 'http://127.0.0.1:8000/customer/login_user/'
    form = RequestForm
# Submit form logic
    submitted = False
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            # **********************************************
            if request.method == 'POST':
                form_first_name = request.POST["student_first_name"]
                form_last_name = request.POST["student_last_name"]
                form_email = request.POST["student_email"]
                form_sn = request.POST["computer_sn"]
                form_os = request.POST['os']
                form_classification = request.POST['computer_classification']
                form_professor_email = request.POST["teacher_email"] 

                # Send email 
                send_mail(
                'Request from ' + form_first_name + ' ' + form_last_name, # subject
                'Please review this request by log in to the dashboard \n Details: \n' +
                'Computer ID: ' + form_sn + '\n' +
                'Operating System: ' + form_os + '\n' +
                'Classification: ' + form_classification + '\n' +
                'Dashboard login: ' + url, # message
                form_email,  # from email
                # ['vcyms.1209@icloud.com'],  # to email
                [form_professor_email],  # to email
                fail_silently=True,
                )
            # ***********************************************
            return HttpResponseRedirect('?submitted=True')
    else: 
        form = RequestForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'request.html', {'form': form, 'submitted': submitted, 'navbar':'request'})

# Students Request View
def student_view(request):
    requests = Request.objects.order_by('-order_date')
    return render(request,'student_request.html', {'requests': list(requests ), 'navbar':'student_view'})

# Teacher Approval View
def teacher_view(request):
     requests = Request.objects.order_by('-order_date')
     return render(request,'teacher_view.html', {'requests': list(requests), 'navbar':'teacher_view'})


def search_request(request):
    if request.method =='POST':
        filter_options = request.POST['status']
        first_name = request.POST['student_f_n']
        last_name = request.POST['student_l_n']
        # Filter by first name
        if filter_options == 'default' and last_name == "":
            select_filter = Request.objects.filter(student_first_name__icontains=first_name)
            return render(request, 'search_request.html', {'select_filter':list(select_filter)})
        # Filter by last name
        if filter_options == 'default' and first_name == "":
            select_filter = Request.objects.filter(student_last_name__icontains=last_name)  
            return render(request, 'search_request.html', {'select_filter':list(select_filter)})
        # Filter by first name and last name
        if (filter_options == 'default' and first_name) and (filter_options == 'default' and last_name):
            select_filter = Request.objects.filter(Q(student_first_name__icontains=first_name) & Q(student_last_name__icontains=last_name))
            return render(request, 'search_request.html', {'select_filter':list(select_filter)})
        else:
            select_filter = Request.objects.filter(order_status=filter_options).filter(student_first_name__icontains=first_name).filter(student_last_name__icontains=last_name)
            # results = select_filter.count()
            return render(request, 'search_request.html', {'select_filter':list(select_filter)})



def approve_request(request, id):
     request_id = Request.objects.get(pk=id)
     form = ApproveForm(request.POST or None, instance=request_id)
     if form.is_valid():
          form.save()
          return redirect('teacher_view')
     return render(request, 'approve_request.html', {'request_id':request_id, 'form': form})

def contact(request):
     if request.method == 'POST':
          form_name = request.POST["form-name"]
          form_email = request.POST["form-email"]
          form_message = request.POST["form-message"]

        # Send email 
          send_mail(
            form_name, # subject
             form_message, # message
             form_email,  # from email
              ['vcyms.dev@gmail.com'],  # to email
              fail_silently=True,
          )
          return render(request, 'contact.html', {'form_name':form_name})
     else:
        return render(request, 'contact.html')

      