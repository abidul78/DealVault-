from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import DisputeSerializer

from deals.models import Deal
from .models import Dispute


class RaiseDisputeView(APIView):

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id)

        except Deal.DoesNotExist:
            return Response(
                {"error": "Deal not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        dispute = Dispute.objects.create(
            deal=deal,
            reason=request.data.get("reason")
        )

        deal.status = "DISPUTED"
        deal.save()

        return Response({
            "message": "Dispute raised successfully",
            "dispute_id": dispute.id
        })
        
class ResolveDisputeView(APIView):

    def post(self, request, dispute_id):

        try:
            dispute = Dispute.objects.get(id=dispute_id)

        except Dispute.DoesNotExist:
            return Response(
                {"error": "Dispute not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        dispute.status = "RESOLVED"
        dispute.save()

        return Response({
            "message": "Dispute resolved"
        })   

class DisputeListView(generics.ListAPIView):

    queryset = Dispute.objects.all()
    serializer_class = DisputeSerializer             