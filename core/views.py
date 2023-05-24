from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Account, TradeDetail
from datetime import datetime, timedelta
import random
from .utils import RepeatedTimer
from time import sleep
from accounts.models import UserProfile
# Create your views here.


def get_percentage_diff(previous, current):
    percentage_difference= ((current - previous)/previous) * 100
    return percentage_difference


def stimulate_profile_and_loss():
    try: 
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

    except:
        print("No Account Found")

    

RepeatedTimer(60, stimulate_profile_and_loss)


@login_required
def dashboard(request):
    context = {}
    try: 
       
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
    except:
        total_trade_return = 0
        total_current_value = 0
        total_cost_basis = 0
        total_portfolio_return = 0
        profit = False

        accounts = Account.objects.all()
        for account in accounts:
            total_current_value = total_current_value + account.current_value
            total_cost_basis = total_cost_basis + account.cost_basis
            total_portfolio_return = total_portfolio_return + account.portfolio_return


        if total_current_value >= total_cost_basis:
            total_trade_return = total_current_value - total_cost_basis
            profit = True
        else:
            total_trade_return = total_cost_basis - total_current_value
            profit = False

        context = {
            'total_current_value': round(total_current_value,2),
            'total_cost_basis': total_cost_basis,
            'accounts': Account.objects.all().count,
            "profit":profit,
            "total_portfolio_return": round(total_portfolio_return, 2),
            "total_trade_return": round(total_trade_return, 2)
        }


    return render(request, 'core/dashboard.html', context)


def customers(request):
    accounts = Account.objects.all()
    formatted_output = []
    counter = 1
    for account in accounts:
        
        user = (UserProfile.objects.get(id=list(account.user_id)[0]))
        
        formatted_output.append({
            "id": counter,
            "name":user.name,
            "cost_basis": account.cost_basis,
            'current_value': account.current_value,
            'porfolio_return':account.portfolio_return,
            'account_id': account.id,
            
        })
        counter=counter+1

    # print(formatted_output)
    context = {
        'accounts': formatted_output,
 
    }
    return render(request, 'core/customer.html', context)


def customer_trade_detail(request, id):
    outcome = []
    trade_time = []
    profit = False
    trade_return = 0
    
    account = Account.objects.get(id = id)
   
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

    user =  UserProfile.objects.get(id=list(account.user_id)[0])


    context = {
        'outcome': outcome,
        'trade_time': trade_time,
        'current_value': account.current_value,
        "portfolio_return":account.portfolio_return,
        "trade_return": round(trade_return,2),
        "profit":profit,
        "user":user,

    }
    return render(request, 'core/customer-trade-detail.html', context)