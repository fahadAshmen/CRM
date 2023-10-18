from django.shortcuts import render, redirect, get_object_or_404
from . forms import LeadForm
from . models import Lead
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def add_lead(request):
    if request.method=='POST':
        form = LeadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by=request.user
            lead.save()
            messages.success(request,'New Lead created')
            return redirect('dashboard')
        # else:
        #     messages.error(request, '')    
    else:
        form=LeadForm()
        return render(request, 'lead/add_lead.html',{'form':form})
    return render(request, 'lead/add_lead.html',{'form':form})


#@login_required
def lead_detail(request, pk):
    lead=get_object_or_404(Lead, created_by=request.user, pk=pk)
    # lead=Lead.objects.filter(created_by=request.user).get(pk=pk) 
    context = {
        'leads': lead,
    }
    return render(request, 'lead/lead_detail.html', context)

def lead_delete(request, pk):
    lead=get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, 'Lead Deleted')
    return redirect('dashboard')

def lead_edit(request, pk):
    lead=get_object_or_404(Lead, created_by=request.user, pk=pk)    
    if request.method =='POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request,'Lead Successfully Changed')
            return redirect('dashboard')
    
    form = LeadForm(instance=lead)        
    context = {
        'form': form,
        'lead': lead,
    }
    return render(request, 'lead/edit_lead.html', context)
