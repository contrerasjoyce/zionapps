from django.shortcuts import render, redirect
from django.http import HttpResponse
from ContrerasList.models import Applicant, School , Admin 
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


def Homerun(request):
    return render(request, 'keps.html')

def Home(request):
    return render(request, 'keps.html')

def Offered(request):
    return render(request, 'login.html')

def Contact(request):
    return render(request, 'contact.html')

def adminlogin(request):
    return render(request, 'userslogin.html')

def Message(request) :
    return render(request, 'results.html')

def require(request):
    return render(request, 'require.html')

def List(request) :
    return render(request,'applicant_list.html')

def View(request) :
    return render(request,'applicant_view.html')

def AdminHome(request):
    return render(request, 'adminaccount.html')


def Homerun_Form(request):
    applicants = Applicant.objects.all()
    return render(request, 'form.html',{'applicants' : applicants})

def new_applicant(request):
    applicants_ = Applicant.objects.create(nFullName=request.POST['CompleteName'],nAddress=request.POST['Address'],aage=request.POST['Aage'],nGenders=request.POST['Gender'],acontumber=request.POST['Cnumber'],aemailAddress=request.POST['EmailAdd'],agname=request.POST['GName'],asoi=request.POST['Occupation'],nAIncome=request.POST['Annual Income'],ausername=request.POST['Usersname'],apassword=request.POST['Passwords'],sstatus=request.POST['stats'])
    return redirect(f'/{applicants_.id}/view_applicant') 

def view_applicant(request, applicant_id):
    applicant_ = Applicant.objects.get(id=applicant_id)
    return render(request, 'school.html', {'applicant': applicant_})


def add_applicant(request,applicant_id):
    applicant_ = Applicant.objects.get(id=applicant_id)
    School.objects.create(NMSchool=request.POST['School'],slevel=request.POST['GradeLevel'],nStudentId=request.POST['StudsId'],nGPA=request.POST['GPA'],sid =request.POST['img'],sgwa=request.POST['img1'],applicant=applicant_)
    return redirect(f'/{applicant_.id}/view_applicant')


def applicant_page(request): 
    if request.method == 'POST':
        if Applicant.objects.filter(ausername=request.POST['Usersname'], apassword=request.POST['Passwords']).exists():
            applicant_ = Applicant.objects.get(ausername=request.POST['Usersname'], apassword=request.POST['Passwords'])
            return redirect(f'/{applicant_.id}/view_applicant')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Offered', context)


def adminaccount(request):
    admins = Admin.objects.all()
    return render(request, 'adminaccount.html', {'admins' : admins})

def applicant_list(request): 
    applicants = Applicant.objects.all() 
    return render(request, 'applicant_list.html',{'applicants' : applicants})

def applicant_view(request, applicant_id):   
    applicant_ = Applicant.objects.get(id=applicant_id)
    school = School.objects.all()
    return render(request, 'applicant_view.html', {'applicant': applicant_,'school' : school})    

def admin_page(request): 
    if request.method == 'POST':
        if Admin.objects.filter(adminu=request.POST['aadminu'], adminp=request.POST['aadminp']).exists():
            admin_ = Admin.objects.get(adminu=request.POST['aadminu'], adminp=request.POST['aadminp'])
            return redirect(f'/adminaccount')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)




def edit(request, id):
    applicants = Applicant.objects.get(id=id)
    context = {'applicants' : applicants}
    return render(request, 'crud.html', context)

def update(request, id):
    applicant= Applicant.objects.get(id=id)
    applicant.sstatus = request.POST['stats']
    applicant.save()
    return redirect ('/applicant_list')

def delete(request, id):
    applicant = Applicant.objects.get(id=id)
    applicant.delete()
    return redirect ('/applicant_list')

