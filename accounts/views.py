from django.shortcuts import render

# Create your views here.

from .models import Accounts

def all_info(request):
    all_info = Accounts.objects.all()
    return render(request, 'account_home.html', {'all_info':all_info})

