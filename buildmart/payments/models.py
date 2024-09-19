from django.db import models
from django.contrib.auth.models import User  
from django.conf import settings

class Payment(models.Model):
    checkout_request_id = models.CharField(max_length=255, unique=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    
    def __str__(self):
        return f"Payment {self.checkout_request_id} - {self.status} by {self.user.username}"
