from django.db import models
from djongo import models
from accounts.models import UserProfile

# Create your models here.

class Account(models.Model):
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user = models.ArrayReferenceField(
        to=UserProfile,
        on_delete=models.CASCADE
    )
    cost_basis = models.FloatField(default=100)
    current_value = models.FloatField(default = 100)
    portfolio_return = models.FloatField(default = 0.00)

    def __str__(self):
        return f"{self.user} | {self.current_value}"
    
class TradeDetail(models.Model):
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account = models.ArrayReferenceField(
        to=Account,
        on_delete=models.CASCADE
    )
    trade_time = models.DateTimeField(auto_now_add=True)
    outcome = models.FloatField() 

    def __str__(self):
        return f"{self.account} | {self.outcome}"   
