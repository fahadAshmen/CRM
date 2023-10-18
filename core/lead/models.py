from django.db import models
from accounts.models import User


class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    LEAD_PRIORITY =(
        (LOW , 'Low'),
        (MEDIUM , 'Medium'),
        (HIGH , 'High')
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    LEAD_STATUS =(
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=12, choices=LEAD_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=12,choices=LEAD_STATUS, default=NEW)
    email = models.EmailField()
    created_by= models.ForeignKey(User, related_name='leads',on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
