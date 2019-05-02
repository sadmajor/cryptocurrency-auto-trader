from django.contrib import admin
from bitcoin.models import History, Account, Action

# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    fields = list_display = ('created_at', 'currency', 'amount')
    readonly_fields = ('created_at', 'amount')

class AccountAdmin(admin.ModelAdmin):
    fields = list_display = ('bitcoint_ammount_with_toman', 'toman_amount')
    readonly_fields = ('bitcoint_ammount', 'toman_amount')
    def bitcoint_ammount_with_toman(self, obj):
        usd_last_history = History.objects.filter(currency='usd').latest('created_at').amount
        bitcoin_last_history = History.objects.filter(currency='bitcoin').latest('created_at').amount
        return "%s (%s)"%(obj.bitcoint_ammount, "{:,}".format(int(obj.bitcoint_ammount * bitcoin_last_history * usd_last_history)))
    bitcoint_ammount_with_toman.short_description = 'مقدار بیت کوین (تومان)'

class ActionAdmin(admin.ModelAdmin):
    fields = list_display = ('timestamp', 'action_type', 'bitcoin_transaction_amount_with_toman', 'usd_price', 'bitcoin_price')
    readonly_fields = ('timestamp', 'action_type', 'bitcoin_transaction_amount', 'usd_price', 'bitcoin_price')
    def bitcoin_transaction_amount_with_toman(self, obj):
        return "%s (%s)"%(obj.bitcoin_transaction_amount, "{:,}".format(int(obj.bitcoin_transaction_amount * obj.usd_price * obj.bitcoin_price)))
    bitcoin_transaction_amount_with_toman.short_description='بیت کوین معامله شده (تومان)'


admin.site.register(Action, ActionAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(History, HistoryAdmin)
