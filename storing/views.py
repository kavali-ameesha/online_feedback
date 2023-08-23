from storing.forms import storingform
from storing.models import storingmodel
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def createstore(request):
    form=storingform()
    if request.method=="POST":
        form=storingform(request.POST)
        name=request.POST.get('name')
        email=(request.POST.get('email'))
        subject = 'welcome to my online feedback app'
        message = f'Hi {name}, Thank you for registering in my webapp.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list )
        form.save()
        return HttpResponse("data is stored")
    return render(request,"home.html",{'form':form})

def readstore(request):
    res=storingmodel.objects.all()
    return render(request,'details.html',{'res':res})

def updatestore(request,pk):
    res=storingmodel.objects.get(id=pk)
    form=storingform(instance=res)
    if request.method=="POST":
        res=storingmodel.objects.get(id=pk)
        form=storingform(request.POST,instance=res)
        form.save()
        return HttpResponse("data is stored")
    return render(request,"home.html",{'form': form})


def deletestore(request,pk):
    res=storingmodel.objects.get(id=pk)
    if request.method=="POST":
        res=storingmodel.objects.get(id=pk).delete()
        return HttpResponse("data is deleted")
    return render(request,"delete_confrim.html",{'res': res})




def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]

        user=User.objects.create_user(
            username=username,
            password=password,
            email=email
        )


        login(request,user)
        subject = 'welcome to GFG world'
        message = f'Hi {User.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [User.email, ]
        send_mail(subject, message, email_from, recipient_list )
        return redirect("/dashboard/")
    return render(request,"signup.html")


