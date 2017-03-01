from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# import view

import sys 
sys.path.append('../')  

from bang_app.models.customer import Customer


class TestRegister(TestCase):
	"""
	Purpose: This class tests matters related to Register

	Methods:
		test_register_should_redirect_to_products

	Author: Abby
	"""


	def test_register_should_redirect_to_products(self):
		response = self.client.get(reverse('bang_app:categories'))
		# response: <HttpResponse status_code=200, "text/html; charset=utf-8">
		self.assertTemplateUsed('categories.html')
		self.assertEqual(response.status_code, 200)




