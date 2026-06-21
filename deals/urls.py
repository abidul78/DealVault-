from django.urls import path
from .views import DealListView, DealCreateView, AcceptDealView

urlpatterns = [
    path('', DealListView.as_view()),
    path('create/', DealCreateView.as_view()),
    path('<int:deal_id>/accept/', AcceptDealView.as_view()),
]