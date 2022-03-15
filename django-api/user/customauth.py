from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework import parsers, renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from user.errors import flatten_validation_error

from user.models import User


class AuthCustomTokenSerializer(serializers.Serializer):

    def validate(self, attrs):
       
        data = self.context['request'].data
        user = User.objects.filter(email=data['email']).first()
        if  user.check_password(data['password']):
            attrs['user'] = user
            return attrs
        else:
            msg = 'Wrong Password'
            raise ValidationError(msg)
  

class CustomObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthCustomTokenSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token = user.create_jwt()

            content = {
                'token': token,
                'user_id': user.id
            }
            return Response(content)
        except ValidationError as e:
            errors = flatten_validation_error(e)
            return Response({
                'msg':errors
            })

def custom_jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
    }
