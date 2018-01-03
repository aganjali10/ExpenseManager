from django.conf.urls import url
from myapp import views

app_name='myapp'

urlpatterns = [
    url(r'^$',views.ExpenseListView.as_view(),name='all'),
    url(r'^expense_detail/(?P<pk>\d+)$',views.ExpenseDetailView.as_view(),name='expense_detail'),
    url(r"new/$", views.CreateExpense.as_view(), name="create"),
]
