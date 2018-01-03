from django import forms
from myapp.models import Expense

class ExpenseForm(forms.ModelForm):

    class Meta():
        model = Expense
        fields = ('title','description','amount','date','username')
