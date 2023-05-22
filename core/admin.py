from django.contrib import admin
from .models import Account, TradeDetail

# Register your models here.

admin.site.register(Account)
@admin.register(TradeDetail)
class TradeDetailAdmin(admin.ModelAdmin):
    list_display= ('account', 'trade_time', 'outcome')
    list_filter = ('outcome',)
    search_fields = ('account', 'trade_time', 'outcome')
