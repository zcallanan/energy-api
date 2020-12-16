from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Yield, PostalCode
from .serializers import StateYieldSerializer

class YieldViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = StateYieldSerializer

    def get_queryset(self):
        if ('capacity' and 'plz') in self.request.query_params:
            # If a DE postal code is a paramater instead of a state, calculate kWh/year
            state = PostalCode.objects.filter(plz = self.request.query_params['plz']).values_list('state', flat=True)
            return Yield.objects.filter(state = state[0])
        return Yield.objects.filter(state = self.request.query_params['state'])


    def pv_yield_list(self, request):
        # State energy yields
        queryset = self.get_queryset()
        # Request context is passed to the serializer in order to do the calculation
        serializer_class = get_serializer_class(queryset, many=True,  context={'request': self.request})
        return Response(serializer_class.data)


