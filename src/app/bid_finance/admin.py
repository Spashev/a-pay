from django.contrib import admin
from bid_finance.models import BidFinance, BidFinanceTye, Transaction, Template

admin.site.register(BidFinance)
admin.site.register(BidFinanceTye)
admin.site.register(Transaction)
admin.site.register(Template)
