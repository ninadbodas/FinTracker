# views.py
from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    # Get soritng paramaters from request
    sort_by = request.GET.get('sort_by')
    sort_order = request.GET.get('sort_order', 'asc') #Default sorting

    # Define default sorting
    default_sorting = 'transaction_date'
    default_order = ''if sort_order.lower() == 'asc' else '-'

    # Apply dynamic sorting to all dataset
    transactions = Transaction.objects.all().order_by(default_order + (sort_by or default_sorting))

    # Context to rtender template
    contxt = {
        'transactions': transactions,
        'sort_by': sort_by,
        'sort_order': sort_order,
    }

    return render(request, 'transactions.html', {'transactions': transactions})

def new_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

def edit_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction_form.html', {'form': form})

def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'confirm_delete.html', {'transaction': transaction})
