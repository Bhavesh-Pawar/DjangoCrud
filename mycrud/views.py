from django.shortcuts import render
from django.http import HttpResponseRedirect
from mycrud.models import Info 
# Create your views here.

class Counter:
    count=0
    def increament(self):
        self.count+=1
        return self.count

def homePage(request):
    return HttpResponseRedirect('/home/')

    
def home(request):
    std=Info.objects.all()
    print(std)
    return render(request,'index.html',{'std':std,'j':Counter()})

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        std=Info.objects.create(name=name,contact=contact)
        std.save()
    return HttpResponseRedirect('/home/')

def deleteData(request,id):
    std=Info.objects.get(pk=id)
    std.delete()
    return HttpResponseRedirect('/home/')

def editPage(request,id):
    std=Info.objects.get(pk=id)
    return render(request,'edit.html',{'std':std,'id':id})

def editData(request,id):
    std=Info.objects.get(pk=id)
    if request.method=='POST':
        e_name=request.POST['name']
        e_contact=request.POST['contact']
        std.name=e_name
        std.contact=e_contact
        std.save()
    return HttpResponseRedirect('/home/')
