from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Yield
import json

class YieldTests(APITestCase):
    fixtures = ["energydump.json"]

    def test_pv_yield_from_state(self):
        """
        Given state, tests the YieldViewSet retrieval of pv_yield kWh/kWp
        """
        client = APIClient()
        response = client.get('/api/pv_yield/', {'state': 'sl'}, format='json')
        expected = {'pv_yield': 1100, 'state': 'sl'}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(json.loads(response.content)[0], expected)
        self.assertEqual(Yield.objects.get(state='sl').state, 'sl')
        self.assertEqual(Yield.objects.get(state='sl').pv_yield, 1100)

    def test_pv_yield_from_plz(self):
        """
        Given plz, tests the YieldViewSet retrieval of pv_yield kWh/kWp
        """
        client = APIClient()
        response = client.get('/api/pv_yield/', {'plz': '08606' }, format='json')
        expected = {'pv_yield': 1120, 'state': 'sn'}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(json.loads(response.content)[0], expected)

    def test_calculation_from_state(self):
        """
        Given state and capacity, tests the YieldViewSet retrieval of calculated kWh/year
        """
        client = APIClient()
        response = client.get('/api/pv_yield/', {'capacity': '10', 'state': 'sl'}, format='json')
        expected = {'pv_yield': 11000, 'state': 'sl'}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(json.loads(response.content)[0], expected)

    def test_calculation_from_plz(self):
        """
        Given plz and capacity, tests the YieldViewSet retrieval of calculated kWh/year
        """
        client = APIClient()
        response = client.get('/api/pv_yield/', {'capacity': '10', 'plz': '08606'}, format='json')
        expected = {'pv_yield': 11200, 'state': 'sn'}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(json.loads(response.content)[0], expected)

