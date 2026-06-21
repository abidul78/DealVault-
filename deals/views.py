from rest_framework import generics
from .models import Deal
from .serializers import DealSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Deal
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsSeller, IsBuyer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
User = get_user_model()

class DealCreateView(generics.CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSeller]

    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    

class AcceptDealView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsBuyer]

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id)

        except Deal.DoesNotExist:
            return Response(
                {"error": "Deal not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        deal.buyer = request.user
        deal.save()

        return Response({
            "message": "Deal accepted successfully"
        })

class DealListView(generics.ListAPIView):

    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]

    filterset_fields = ['status']
    search_fields = ['title']
 