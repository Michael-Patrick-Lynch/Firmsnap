from django.test import TestCase, Client
from django.urls import reverse
from app.views import SHARED_SECRET
from .models import Organisation

class NewOrgEndpointTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('new_org')

        self.headers = {
            'HTTP_AUTHORIZATION': f'Bearer {SHARED_SECRET}',
            'CONTENT_TYPE': 'application/json'
        }

    def test_create_organisation_success(self):
        """Test creating a new organisation successfully"""
        response = self.client.post(
            self.url,
            data={'org_name': 'Microsoft'},
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Organisation created successfully')
        self.assertTrue(Organisation.objects.filter(org_name='Microsoft').exists())

    def test_missing_org_name(self):
        """Test that a missing org_name returns a 400 error"""
        response = self.client.post(
            self.url,
            data={},
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('org_name is required', response.json()['error'])

    def test_invalid_json_format(self):
        """Test that invalid JSON format returns a 400 error"""
        response = self.client.post(
            self.url,
            data='invalid-json',
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Invalid JSON format')

    def test_unauthorized_access(self):
        """Test that a request without the correct token returns a 401 error"""
        response = self.client.post(
            self.url,
            data={'org_name': 'Unauthorized Test'},
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer wrong-token'
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['error'], 'Unauthorized')
