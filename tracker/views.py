from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    total_income = transactions.filter(category__type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(category__type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    # Data for charts
    expenses_by_category = transactions.filter(category__type='EXPENSE').values('category__name').annotate(total=Sum('amount'))
    
    chart_labels = [item['category__name'] for item in expenses_by_category]
    chart_data = [round(float(item['total']), 2) for item in expenses_by_category]

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'recent_transactions': transactions.order_by('-date')[:5]
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(user=request.user)
    return render(request, 'tracker/transaction_form.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'tracker/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            # Jeśli user chce tylko dodać kategorię do transakcji, wygodniej byłoby wracać tam
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tracker/category_form.html', {'form': form})
