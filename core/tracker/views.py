from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Transaction
from .forms import TransactionForm
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

DEFAULT_CATEGORIES = [
    'Salary',
    'Freelance',
    'Bonus',
    'Business',
    'Gift Received',
    'Interest',
    'Investment',
    'Rental Income',
    'Food',
    'Groceries',
    'Dining Out',
    'Transport',
    'Utilities',
    'Rent',
    'EMI',
    'Insurance',
    'Education',
    'Shopping',
    'Clothing',
    'Healthcare',
    'Entertainment',
    'Travel',
    'Subscriptions',
    'Taxes',
    'Mobile Recharge',
    'Pets',
    'Personal Care',
    'Home Maintenance',
    'Charity',
    'Other',
]

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    income = transactions.filter(transaction_type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = transactions.filter(transaction_type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'transactions': transactions,
        'balance': income - expense,
        'income': income,
        'expense': expense
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_transaction(request):
    if not Category.objects.exists():
        Category.objects.bulk_create([Category(name=name) for name in DEFAULT_CATEGORIES])

    form = TransactionForm(request.POST or None)
    if form.is_valid():
        transaction = form.save(commit=False)
        transaction.user = request.user
        transaction.save()
        return redirect('dashboard')
    return render(request, 'tracker/transaction_form.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})