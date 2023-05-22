from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Account, TradeDetail
from datetime import datetime, timedelta
import random
from .utils import RepeatedTimer
from time import sleep
# Create your views here.


def get_percentage_diff(previous, current):
    percentage_difference= ((current - previous)/previous) * 100
    return percentage_difference


def stimulate_profile_and_loss():
    accounts =  Account.objects.all()
  
    current_time = datetime.now()

    for account in accounts:
        time = current_time 
        profit_loss = round(random.uniform(-100, 100), 2)
        TradeDetail.objects.create(account_id=account.user_id, trade_time=time, outcome=profit_loss)

        obj = get_object_or_404(Account, user_id = list(account.user_id)[0])
        obj.current_value = round(obj.current_value + profit_loss,2)
        obj.portfolio_return = round(get_percentage_diff(obj.cost_basis, obj.current_value),2)
        obj.save()

RepeatedTimer(60, stimulate_profile_and_loss)


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')