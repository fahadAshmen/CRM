from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from lead.models import Lead

@login_required(login_url='/accounts/login/')
def dashboard(request):
    lead = Lead.objects.filter(created_by=request.user) #created_by=request.user
    context={
        'leads':lead
    }
    return render(request, 'dashboard/dashboard.html', context)
