from django.forms import ValidationError
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_auth.views import LoginView as RestLoginView
from user.errors import flatten_validation_error
from .serializer import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator


class CreateUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        try:
            fields = {
                'email':data.get('email'),
                'password':data.get('password'),
                'phone':data.get('phone'),
                'first_name':data.get('first_name'),
                'last_name':data.get('last_name'),
            }
            
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            new_user = User.objects.create_user(**fields)
            token = new_user.create_jwt()
            return Response({
                'token': token,
                'user_data': UserSerializer(new_user).data,
            }, status=status.HTTP_201_CREATED)

        except ValidationError as e:    
            print(e)
            errors = flatten_validation_error(e)
            return Response({
                'msg':errors
            })


class RetrieveLocation(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    lookup_field = 'id'


    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60*2))
    def dispatch(self, *args, **kwargs):
        return super(RetrieveLocation, self).dispatch(*args, **kwargs)
    
    
    def create(self,request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'msg':'Success'})
        except Exception as e:
            print(e)
            return Response({'msg':"Error TO Save Location"},status=status.HTTP_400_BAD_REQUEST)