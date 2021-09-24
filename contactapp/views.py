from django.db import models
from django.http.response import HttpResponse
from .models import contact
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def addpage(request):
    return render(request,'add.html')


def updatepage(request):
    return render(request,'update.html')

def displaypage(request):
    return render(request,'display.html')

def deletepage(request):
    return render(request,'delete.html')

def addContact(request):
    msgdic={ }
    try:
        Name=request.POST["name"]
        Number=request.POST["number"]
        namecheck=contact.objects.filter(name=Name)        
        numbercheck=contact.objects.filter(number=Number)
        if numbercheck.exists() or namecheck.exists(): 
            print("Contact exist")
            msgdic["msg1"]="Contact Already Exists"
            
        else:
            print("Contact not exist")
            contactlist=contact(name=Name,number=Number)
            contactlist.save()
            msgdic["msg1"]="Contact Added"
            
        return render(request,'add.html',msgdic)
    except Exception as e:
        print("EXCEPTION:",e)
        msgdic["msg1"]="Contact Not Added"
        return render(request,'add.html',msgdic)

def deleteContact(request):
    msgdic={}
    try:
        Name=request.POST['name']
        contactname=contact.objects.get(name=Name)
        contactname.delete()
        msgdic["msg2"]="Contact deleted"
        return render(request,"delete.html",msgdic)

    except Exception as e:
        msgdic["msg2"]="Contact Not Deleted"
        return render(request,"delete.html",msgdic)


def updateContact(request):#change number or name or both

    updatemsg={}
    try:
        newname=request.POST["newname"]
        newnumber=request.POST["newnumber"]
        name=request.POST["name"]
        print(name)
        namecheck=contact.objects.filter(name=name)
        print(namecheck)
        if namecheck.count()!=0:
            newnamecheck=contact.objects.filter(name=newname)
            if newnamecheck.count()!=0:#if update name
                print("Name Exist")
                updatemsg["msg"]="Contact Exist"
            else:
                print("NEWNAME:",newname)
                contact.objects.filter(name=name).update(name=newname)
                name=newname  #useful if changing both number and name
                updatemsg["msg"]="Contact Updated"

            if newnumber:#if update number
                print("NEW NUMBER:",newnumber)
                numbercheck=contact.objects.filter(number=newnumber)
                if numbercheck.exists(): #check number exist in db
                    print("number exist")
                    updatemsg["msg"]="Number Already Exists"
                else:
                    print("number not exist")
                    contact.objects.filter(name=name).update(number=newnumber)
                    updatemsg["msg"]="Contact Updated "

            return render(request,"update.html",updatemsg)
        else:
            print("name notfound")
            updatemsg["msg"]="Contact name not found"
            return render(request,"update.html",updatemsg)

    except Exception as e:
        print(e)
        updatemsg["msg"]="Contact not updated"
        return render(request,"update.html",updatemsg)



def displayContact(request):
    try:
        contactobj=contact.objects.all()
        print(contactobj)
        return render(request,"display.html",{"contact":contactobj,"name1":"Name","contact1":"Contact"})
    except Exception as e:
        return HttpResponse("Error")
        



    
