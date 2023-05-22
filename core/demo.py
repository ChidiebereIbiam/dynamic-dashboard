from datetime import datetime, timedelta
import random

def get_percentage_diff(previous, current):
    percentage_difference= ((current - previous)/previous) * 100
    return percentage_difference

def stimulate_profile_and_loss():
    accounts =  ["Chidiebere"]
    current_time = datetime.now()
    ammount = 130
    current_amount = 130
    percentage = 0

    for account in accounts:
        # for i in range(5):
        time = current_time 
        profit_loss = round(random.uniform(-100, 100), 2)
        

        # if profit_loss >= 0:
        #     current_amount = current_amount + profit_loss
        # else:
        #     current_amount = current_amount - profit_loss
        
        current_amount = current_amount + profit_loss
        percentage = get_percentage_diff(ammount, current_amount)
        print(f"{account} = {profit_loss} | {time}")
        print("Percetage =", round(percentage, 2))
        print("Current Amount=", current_amount)
        
    if current_amount >= ammount:
        print("Your Profit is:", current_amount-ammount)
    else:
        print("Your Lost is:", ammount - current_amount)
            # trade = TradeDetail(account=account, tradetime=time, outcome=profit_loss)
            # trade.save()
            # obj = get_object_or_404(Account, user = account.user)
            # obj.current_value = 
            # obj.portfolio_return =
            # obj.save()

# stimulate_profile_and_loss()

import threading 
import time

class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False


from time import sleep

def hello(name="World"):
    print ("Hello %s!" % name)
    print(datetime.now())

print ("starting...")
rt = RepeatedTimer(60, stimulate_profile_and_loss) # it auto-starts, no need of rt.start()
try:
    sleep(255) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!

    
