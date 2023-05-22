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

# RepeatedTimer(60, stimulate_profile_and_loss)


@login_required
def dashboard(request):
    outcome = []
    trade_time = []
    profit = False
    trade_return = 0
    
    account = Account.objects.get(user_id = request.user.id)
    stimulation = TradeDetail.objects.filter(account_id =account.id).order_by('trade_time')
    for stimu in stimulation:
        trade_time.append(stimu.trade_time.strftime("%H:%M:%S"))
        outcome.append (stimu.outcome)

    if account.current_value >= account.cost_basis:
        trade_return = account.current_value - account.cost_basis
        profit = True
    else:
        trade_return = account.cost_basis - account.current_value
        profit = False


    context = {
        'outcome': outcome,
        'trade_time': trade_time,
        'current_value': account.current_value,
        "portfolio_return":account.portfolio_return,
        "trade_return": round(trade_return,2),
        "profit":profit,

    }

    return render(request, 'core/dashboard.html', context)