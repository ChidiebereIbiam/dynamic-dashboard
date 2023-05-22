from django.db.models.signals import post_save
from .models import UserProfile
from core.models import Account

def account(sender, instance, created,**kwargs):
     if created:
        
        Account.objects.create(
            user_id=[instance.id],
        )

post_save.connect(account, sender=UserProfile)