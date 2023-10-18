from django.urls import path
from dashboard import views
from lead.views import add_lead, lead_detail, lead_delete, lead_edit

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('add-lead/',add_lead,name='add-lead'),
    path('lead-detail/<int:pk>/',lead_detail,name='lead-detail'),
    path('lead-edit/<int:pk>/',lead_edit,name='lead-edit'),
    path('lead-delete/<int:pk>/',lead_delete,name='lead-delete'),
]
