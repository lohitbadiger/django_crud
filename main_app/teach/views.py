from django.shortcuts import render,redirect

# Create your views here.
from . models import AllInfo 

from . forms import AllInfoForm
def home(request):
    
    all_items=AllInfo.objects.all()
    
    return render(request,'teach/all_items.html',{'all_items':all_items}) 


def create_info(request):
    form=AllInfoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request,'teach/all-product-form.html',{'form':form})



def update_info(request,id):
    all_items=AllInfo.objects.get(id=id)
    form=AllInfoForm(request.POST or None, instance=all_items)
        
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request,'teach/all-product-form.html', {'form':form, 'all_items':all_items})


def delete_info(request,id):
    delete_info=AllInfo.objects.get(id=id)
    
    if request.method=='POST':
       delete_info.delete()
       return redirect(home)
    return render(request, 'teach/info-delete.html',{'delete_info':delete_info})
