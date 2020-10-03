from django.shortcuts import render
from .models import Expense
from django.views.generic import CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.forms import ExpenseForm
from django.urls import reverse_lazy
# Create your views here.

class ExpenseListView(ListView):
    model = Expense
    def get_queryset(self):
        return Expense.objects.order_by('-date')

class ExpenseDetailView(DetailView):
    model = Expense

class CreateExpense(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'myapp/expense_detail.html'
    #form_class = ExpenseForm
    fields = ['title', 'amount', 'description', 'username']
    model = Expense
    success_url = reverse_lazy("myapp:all")
