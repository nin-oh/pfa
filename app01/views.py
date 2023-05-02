from django.http import HttpResponseRedirect
from django.shortcuts import render



def acc(request):
    return render(request, 'app01/page_acc.html')




