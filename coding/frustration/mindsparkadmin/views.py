from django.db.models import Count, Avg
from django.shortcuts import render, redirect


# Create your views here.
from mindsparkadmin.forms import NotificationForm
from user.models import AnswerModel, RegistrationModel, FeedbackModel


def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('viewuserdetails')
    return render (request,'mindsparkadmin/login.html')
def homepage(request):
    return render(request,'mindsparkadmin/homepage.html')
def chartpage(request,chart_type):
    chart = AnswerModel.objects.values('catagory').annotate(s1=Avg('sessionone'),s2=Avg('sessiontwo'),s3=Avg('sessionthree'),s4=Avg('sessionfour'),s5=Avg('sessionfive'))
    return render(request,'mindsparkadmin/chart.html',{'chart_type':chart_type,'object':chart})

def viewuserdetails(request):
    obj = RegistrationModel.objects.all()
    return render(request,'mindsparkadmin/viewuserdetails.html',{'objects':obj})

def notification(request):
    if request.method == "POST":
        forms = NotificationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('notification')
    else:
        forms = NotificationForm()

    return render(request,'mindsparkadmin/notification.html',{'form':forms})

def viewfeedback(request):
    obj = FeedbackModel.objects.all()
    return render(request,'mindsparkadmin/viewfeedback.html',{'object':obj})

def motivationalaresults(request):
    chart = AnswerModel.objects.values('catagory').annotate(s1=Avg('sessionone'), s2=Avg('sessiontwo'),
                                                            s3=Avg('sessionthree'), s4=Avg('sessionfour'),
                                                            s5=Avg('sessionfive'))
    return render(request,'mindsparkadmin/motivationalaresults.html',{'objects':chart})

