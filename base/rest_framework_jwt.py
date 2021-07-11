import datetime
from rest_framework.views import APIView
from base.response import json_ok_response, json_error_response
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer, VerifyJSONWebTokenSerializer, \
    RefreshJSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER



class Base(JSONWebTokenAPIView):
    """
    Base API View that various JWT interactions inherit from.
    """
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_context(self):
        return super(Base, self).get_serializer_context()

    def post(self, request, *args, **kwargs):
        serializer = super(Base, self).post(request, *args, **kwargs)
        return json_ok_response(serializer.data)


class ObtainJSONWebToken(Base):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


class VerifyJSONWebToken(Base):
    """
    API View that checks the veracity of a token, returning the token if it
    is valid.
    """
    serializer_class = VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(Base):
    """
    API View that returns a refreshed token (with new expiration) based on
    existing token

    If 'orig_iat' field (original issued-at-time) is found, will first check
    if it's within expiration window, then copy it to the new token
    """
    serializer_class = RefreshJSONWebTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()
