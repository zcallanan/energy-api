from rest_framework import serializers
from .models import Yield, PostalCode

class StateYieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yield
        fields = [ 'pv_yield', 'state']

class CapacitySerializer(serializers.ModelSerializer):

    pv_yield = serializers.SerializerMethodField()
    plz = serializers.SerializerMethodField()

    class Meta:
        model = Yield
        fields = ('pv_yield', 'plz')

    def get_pv_yield(self, obj):
        if self.context['request'].query_params['capacity']:
            # Return (pv_yield: calculated kWh/year)
            return (int(obj.pv_yield) * int(self.context['request'].query_params['capacity']))

    def get_plz(self, obj):
        # Return (plz: state_name)
        return obj.state




