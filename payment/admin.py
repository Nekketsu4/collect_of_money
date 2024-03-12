from django.contrib import admin

from payment.models import Payment

@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    pass
