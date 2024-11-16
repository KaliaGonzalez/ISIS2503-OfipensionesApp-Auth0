from django.shortcuts import render
from .forms import BalanceForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_measurement import create_balance, get_balances
from django.contrib.auth.decorators import login_required

@login_required
def balance_list(request):
    balances = get_balances()
    context = {
        'balance_list': balances
    }
    return render(request, 'Balance/balances.html', context)

def measurement_create(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            create_balance(form)
            messages.add_message(request, messages.SUCCESS, 'Balance creado con exito ')
            return HttpResponseRedirect(reverse('balanceCreate'))
        else:
            print(form.errors)
    else:
        form = BalanceForm()

    context = {
        'form': form,
    }

    return render(request, 'Balance/balanceCreate.html', context)