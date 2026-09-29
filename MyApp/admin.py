from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'expense_id',
        'expense_name',
        'category',
        'amount',
        'date',
        'payment_method',
    )

    search_fields = (
        'expense_name',
        'category',
        'payment_method',
        'notes',
    )

    list_filter = (
        'category',
        'payment_method',
        'date',
    )

    ordering = (
        '-date',
        '-expense_id',
    )