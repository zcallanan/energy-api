from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Yield, PostalCode
from .serializers import StateYieldSerializer
from rest_framework.renderers import JSONRenderer

class YieldViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = StateYieldSerializer
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        if ('plz') in self.request.query_params:
            # If a DE postal code is a paramater instead of a state, determine the state, then do calculation
            state = PostalCode.objects.filter(plz = self.request.query_params['plz']).values_list('state', flat=True)
            if state:
                return Yield.objects.filter(state = state[0])
            raise Http404("PLZ does not exist")
        elif ('state' or 'plz') not in self.request.query_params:
            # If state or plz are not params, then raise 404
            raise Http404("No State or PLZ provided")

        # If state is provided, filter by it
        result = Yield.objects.filter(state = self.request.query_params['state'])

        if result:
            return result

        raise Http404("State does not exist")


    def pv_yield_list(self, request):
        # State energy yields
        queryset = self.get_queryset()
        # Request context is passed to the serializer in order to do the calculation
        serializer_class = get_serializer_class(queryset, many=True,  context={'request': self.request})
        return Response(serializer_class.data)


