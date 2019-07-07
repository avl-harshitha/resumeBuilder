from django.shortcuts import render
from django.shortcuts import render, redirect
import logging
from .models import ResDetails,UserLogin
from .forms import ResumeForm,LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
def home(request):
    return render(request,'resume/home.html',data)
@csrf_exempt
#remove this
def create(request):
    # form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
                form.save()
                # details = ResDetails.objects.all().filter(FirstName='Harshitha').filter(LastName='Annamraju').first()
                # data = {
                #         'page_title': 'final',
                #         'details': details
                #         }
                # # print(details.LastName)
                # print(type(details))
                return render(request,'resume/templatelist.html')
        
                #print form invalid
            
    else:
        form = ResumeForm()
        return render(request,'resume/create.html',{'form':form})

def template1(request):
        if request.method == 'POST':
                form = LoginForm(request.POST)
                print(request.POST['FirstNameLogin'])
                if form.is_valid():
                        details = ResDetails.objects.all().filter(FirstName=request.POST['FirstNameLogin']).first()
                        # summarylist = details.summary.split('.')
                        data = {
                                'person': details
                                # 'summaryone':summarylist[0]
                                # 'summarytwo':summarylist[1]
                                # 'summarythree':summarylist[2]
                                

                                }
                        print(details.DateOfBirth)
                        print(type(details))
                        return render(request,'resume/template1.html',data)
        else:
                form = LoginForm()
                return render(request,'resume/confirmedlogin1.html',{'form':form})


def template2(request):
        if request.method == 'POST':
                form = LoginForm(request.POST)
                print(request.POST['FirstNameLogin'])
                if form.is_valid():
                        details = ResDetails.objects.all().filter(FirstName=request.POST['FirstNameLogin']).first()
                        # summarylist = details.summary.split('.')
                        data = {
                                'person': details
                                # 'summaryone':summarylist[0]
                                # 'summarytwo':summarylist[1]
                                # 'summarythree':summarylist[2]
                                }
                        print(details.DateOfBirth)
                        print(type(details))
                        return render(request,'resume/template2.html',data)
        else:
                form = LoginForm()
                return render(request,'resume/confirmedlogin2.html',{'form':form})

def template3(request):
        if request.method == 'POST':
                form = LoginForm(request.POST)
                print(request.POST['FirstNameLogin'])
                if form.is_valid():
                        details = ResDetails.objects.all().filter(FirstName=request.POST['FirstNameLogin']).first()
                        # summarylist = details.summary.split('.')
                        data = {
                                'person': details
                                # 'summaryone':summarylist[0]
                                # 'summarytwo':summarylist[1]
                                # 'summarythree':summarylist[2]
                                }
                        print(details.DateOfBirth)
                        print(type(details))
                        return render(request,'resume/template3.html',data)
        else:
                form = LoginForm()
                return render(request,'resume/confirmedlogin3.html',{'form':form})



