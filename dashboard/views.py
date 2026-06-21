from rest_framework.views import APIView
from rest_framework.response import Response

from deals.models import Deal


class DashboardView(APIView):

    def get(self, request):

        return Response({
            "total_deals": Deal.objects.count(),

            "completed_deals":
            Deal.objects.filter(
                status="COMPLETED"
            ).count(),

            "disputed_deals":
            Deal.objects.filter(
                status="DISPUTED"
            ).count()
        })