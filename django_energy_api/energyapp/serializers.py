from rest_framework import serializers
from .models import Yield

class StateYieldSerializer(serializers.ModelSerializer):

    pv_yield = serializers.SerializerMethodField()

    class Meta:
        model = Yield
        fields = ['pv_yield', 'state']
        read_only_fields = ['pv_yield', 'state']

    def get_pv_yield(self, obj):
        if self.context['request'].query_params.get('capacity'):
            # Return (pv_yield: calculated kWh/year)
            return (int(obj.pv_yield) * int(self.context['request'].query_params.get('capacity')))
        return int(obj.pv_yield)
