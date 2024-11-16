from ..models import Balance

def get_balances():
    queryset = Balance.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_balance(form):
    balance = form.save()
    balance.save()
    return ()