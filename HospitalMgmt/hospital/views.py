from hospital.forms import Addoctorform
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from hospital.models import *
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()
    beds=Beds.objects.all()
    d=0
    p=0
    a=0
    b=0
    for i in doctors:
        d=d+1
    
    for i in patient:
        p=p+1
    
    for i in appointment:
        a=a+1
    for i in beds:
        b=b+1
    d1={'d':d,'p':p,'a':a,'b':b}


    return render(request,'index.html',d1)
    

def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)

def Add_Doctor(request):
    if request.user.is_staff:
        user=request.user
        form=Addoctorform(request.POST)
        context={"form":form}
        if form.is_valid():
            to=form.save(commit=False)
            to.user=user
            to.save()
            return redirect('view_doctor')
        else:
            return render(request,'add_doctor.html',context)



def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')




def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    d={'pat':pat}
    return render(request,'view_patient.html',d)



def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        g=request.POST['gender']
        a=request.POST['address']
        i=request.POST['issue']
        jd=request.POST['joining_date']
        
        try:

            Patient.objects.create(name=n,mobile_no=c,gender=g,address=a,issue=i,joining_date=jd)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_patient.html',d)

def Add_Bill(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    patient1=Patient.objects.all()

    if request.method=='POST':
        p=request.POST['patient']
        a=request.POST['amount']
        d=request.POST['date']
        s=request.POST['status']
        patient=Patient.objects.filter(name=p).first()
            
        try:
            Bill.objects.create(patient=patient,amount=a,date=d,status=s)
            error="no"
        except:
            error="yes"
    d={'patient':patient1,'error':error}
    return render(request,'add_bill.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def Delete_Bill(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    bill=Bill.objects.get(id=pid)
    bill.delete()
    return redirect('view_bill')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    ap=Appointment.objects.all()
    d={'ap':ap}
    return render(request,'view_appointment.html',d)

def View_Beds(request):
    if not request.user.is_staff:
        return redirect('login')
    ap=Beds.objects.all()
    d={'ap':ap}
    return render(request,'view_beds_availability.html',d)

def View_Bill(request):
    if not request.user.is_staff:
        return redirect('login')
    b=Bill.objects.all()
    d={'b':b}
    return render(request,'view_bill.html',d)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()

    if request.method=='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        d1=request.POST['date1']
        t=request.POST['time1']
        s=request.POST['status']
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t,status=s)
            error="no"
        except:
            error="yes"
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)


def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')

def Delete_Bed(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    beds=Beds.objects.get(id=pid)
    beds.delete()
    return redirect('view_beds_availability')