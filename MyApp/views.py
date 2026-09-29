from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    expenses = Expense.objects.all().order_by('-date', '-expense_id')

    total_amount = Expense.objects.aggregate(
        total=Sum('amount')
    )['total'] or 0

    return render(request, 'MyApp/expenses_list.html', {
        'expenses': expenses,
        'total_amount': total_amount,
    })


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'MyApp/expense_form.html', {
        'form': form,
        'page_title': 'Add New Expense',
        'button_text': 'Add Expense',
    })


def edit_expense(request, expense_id):
    expense = get_object_or_404(
        Expense,
        expense_id=expense_id
    )

    if request.method == 'POST':
        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'MyApp/expense_form.html', {
        'form': form,
        'page_title': 'Edit Expense',
        'button_text': 'Update Expense',
    })


def delete_expense(request, expense_id):
    expense = get_object_or_404(
        Expense,
        expense_id=expense_id
    )

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(request, 'MyApp/expense_confirm_delete.html', {
        'expense': expense,
    })