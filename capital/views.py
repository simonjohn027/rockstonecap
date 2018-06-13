from django.shortcuts import render,get_object_or_404
from .models import *




def index(request):
    return render(request, 'capital/index.html')

def about(request):
    return render(request, 'capital/about.html')


def dashboardView(request,user_id):
    person = get_object_or_404(User, pk=user_id)
    data = person.clientportfolio_set.all()
    balances = []
    principal_amounts = []
    returns = []

    number = len(data)
    for i in range(number):
        balances.append(float(data[i].currentBalance))
        principal_amounts.append(float(data[i].principalAmount))
        returns.append(float(data[i].growth()))
    if number != 0 :
        totalreturns = round(sum(returns)/number,2)
    else:
        totalreturns = round(sum(returns) / 1, 2)

    currentbalance = round(sum(balances),2)

    investedAmount = sum(principal_amounts)
    context = {
        'investedAmount':investedAmount,
        'lastBalances':balances,
         'balance':currentbalance,
        'returns':totalreturns
    }
    return render(request, 'capital/dashboard.html', context)
