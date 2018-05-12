from django.test import TestCase
from .models import Products
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.product_name = "Pilopastas"
        self.product_store = "Plaza"
        self.products = Products(name=self.product_name,
                                 store_name=self.product_store
                                 )

    def test_model_can_create_a_product(self):
        """Test the Products model can create a products."""
        old_count = Products.objects.count()
        self.products.save()
        new_count = Products.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.product_data = {'name': 'No se', 'store_name': 'tampoco se'}
        self.response = self.client.post(
            reverse('create'),
            self.product_data,
            format="json")

    def test_api_can_create_a_product(self):
        """Test the api has product creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
