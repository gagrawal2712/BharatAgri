from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from common.exceptions import Exception400
from rest_framework.response import Response


class SignIn(APIView):
    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                return Response('already logged in')
            params = request.data
            username = params.get('username')
            password = params.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                raise Exception400('invalid credentials')
            return Response('logged in')
        except Exception as e:
            raise Exception400(e)
    
class SignOut(APIView):
    def post(self, request):
        logout(request)
        return Response('logged out')
    
                