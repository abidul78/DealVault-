from django.urls import path
from .views import RaiseDisputeView, ResolveDisputeView, DisputeListView


urlpatterns = [
    path('', DisputeListView.as_view()),
    path('<int:deal_id>/raise/', RaiseDisputeView.as_view()),
    path('<int:dispute_id>/resolve/', ResolveDisputeView.as_view()),
]