from django.contrib import admin
from bitcoin.models import History, Account, Action

# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    fields = list_display = ('created_at', 'currency', 'amount')
    readonly_fields = ('created_at', 'amount')

class AccountAdmin(admin.ModelAdmin):
    fields = list_display = ('bitcoint_ammount', 'toman_amount',)
    readonly_fields = ('bitcoint_ammount', 'toman_amount')

class ActionAdmin(admin.ModelAdmin):
    fields = list_display = ('timestamp', 'action_type', 'bitcoin_transaction_amount', 'usd_price', 'bitcoin_price')
    readonly_fields = ('timestamp', 'action_type', 'bitcoin_transaction_amount', 'usd_price', 'bitcoin_price')

admin.site.register(Action, ActionAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(History, HistoryAdmin)
