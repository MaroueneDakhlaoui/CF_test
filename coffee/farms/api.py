from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Farm
from rest_framework import viewsets, permissions
from .serializers import FarmSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# Farm ViewSet
# A view set allows us to create a full CRUD API without having to specify explicit methods

class FarmViewSet(viewsets.ViewSet):
    #authentication_classes = (SessionAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Farm.objects.all()
        serializer = FarmSerializer(queryset, many=True)
        return Response(serializer.data)

    def myfarms(self, request):
        active_user = self.request.user.id
        print("------------------------------")
        print(active_user)
        queryset = Farm.objects.filter(owner_id=active_user)
        serializer = FarmSerializer(queryset, many=True)
        return Response(serializer.data)
