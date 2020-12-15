from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Yield, PostalCode
from .serializers import StateYieldSerializer, CapacitySerializer

class YieldViewSet(viewsets.ReadOnlyModelViewSet):

    def get_serializer_class(self):
      # Determine serializer
        return CapacitySerializer if 'capacity' in self.request.query_params else StateYieldSerializer


    def get_queryset(self):
        if 'capacity' in self.request.query_params:
            state = PostalCode.objects.filter(plz = self.request.query_params['plz']).values_list('state', flat=True)
            queryset = Yield.objects.filter(state = state[0])
        else:
            queryset = Yield.objects.filter(state = self.request.query_params['state'])
        return queryset


    def pv_yield_list(self, request):
        # State energy yields
        queryset = self.get_queryset()
        serializer_class = get_serializer_class(queryset, many=True,  context={'request': self.request})
        return Response(serializer_class.data)


