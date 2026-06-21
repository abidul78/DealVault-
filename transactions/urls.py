from django.urls import path
from .views import (
    DepositMoneyView,
    ReleaseMoneyView,
    RefundMoneyView,
    TransactionListView
)

urlpatterns = [
    path('', TransactionListView.as_view()),
    path('<int:deal_id>/deposit/', DepositMoneyView.as_view()),
    path('<int:deal_id>/release/', ReleaseMoneyView.as_view()),
    path('<int:deal_id>/refund/', RefundMoneyView.as_view()),
]