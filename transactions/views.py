from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from deals.models import Deal
from .models import Transaction
from rest_framework import generics
from .serializers import TransactionSerializer


class DepositMoneyView(APIView):

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id)

        except Deal.DoesNotExist:
            return Response(
                {"error": "Deal not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        transaction = Transaction.objects.create(
            deal=deal,
            amount=deal.amount,
            status='HELD'
        )

        deal.status = 'FUNDS_HELD'
        deal.save()

        return Response({
            "message": "Money deposited successfully",
            "transaction_id": transaction.id
        })

class ReleaseMoneyView(APIView):

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id)

        except Deal.DoesNotExist:
            return Response(
                {"error": "Deal not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            transaction = Transaction.objects.get(deal=deal)

        except Transaction.DoesNotExist:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        transaction.status = 'RELEASED'
        transaction.save()

        deal.status = 'COMPLETED'
        deal.save()

        return Response({
            "message": "Money released successfully"
        })        

        
class RefundMoneyView(APIView):

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id)

        except Deal.DoesNotExist:
            return Response(
                {"error": "Deal not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            transaction = Transaction.objects.get(deal=deal)

        except Transaction.DoesNotExist:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        transaction.status = "REFUNDED"
        transaction.save()

        deal.status = "COMPLETED"
        deal.save()

        return Response({
            "message": "Money refunded successfully"
        }) 

class TransactionListView(generics.ListAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer               