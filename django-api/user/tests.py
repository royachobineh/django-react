from audioop import reverse
from django.test import TestCase

import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase,APIClient

from .models import User,Location

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

class Locationtest(APITestCase):
    def setUpLocation(self):
        self.data = {
           'name':'Mymensingh',
            'latitude':'24.934725',
            'longitude':'90.751511',}
        location = Location(**self.data)
        location.save()



    def test_api_jwt(self):
    

        resp = self.client.post('/user/register/',{'first_name':'testuser',
            'last_name':'example',
            'email':'testuser@gmail.com',
            'password':'123456',
	        'phone': '+9199999999'
        }, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

     

        resp = self.client.post('/user/login/', {'email':'testuser@gmail.com', 'password':'123456'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']
        #print(token)

       
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
        resp = client.get('/user/location/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        resp = client.get('/user/location/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)



class RegisterUser(APITestCase):
    def test_new_user(self):

        # CREATE USER
        user_response = self.client.post('/user/register/',{
            'first_name':'testuser',
            'last_name':'example',
            'email':'testuser@gmail.com',
            'password':'123456',
	        'phone': '+9199999999'
        })
        print(f'\n\n\nUSER RESPONSE: {json.loads(user_response.content)}')
        self.assertEqual(user_response.status_code, status.HTTP_201_CREATED)

class LocationTest(TestCase):
    
    def setUp(self):
        self.credentials = {
            'first_name':'testuser',
            'last_name':'example',
            'email':'testuser@gmail.com',
            'password':'123456',
	        'phone': '+9199999999'}
        User.objects.create_user(**self.credentials)
   
  
