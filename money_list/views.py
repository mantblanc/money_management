from django.shortcuts import render, redirect
from .models import MoneyTransaction
from .forms import MoneyForm

from django.views import View
from django.views import generic

# Create your views here.

class money_list(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'money_list/list.html'
        money_transaction = MoneyTransaction.objects.all()
        return render(request, template_name, {"money_transaction": money_transaction})

def check_post(request):
    template_name = 'money_list/money_list_success.html'
    if request.method == "POST":
        form = MoneyForm(request.POST)
        if form.is_valid():
            money = form.save(commit=False)
            money.money_save()
            message = "목록을 추가하였습니다."
            return render(request, template_name, {"message": message})
    else:
        template_name = 'money_list/money_list_insert.html'
        form = MoneyForm
        return render(request, template_name, {"form" : form})