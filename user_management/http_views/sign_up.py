from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from common.exceptions import Exception400

class SignUp(APIView):
    def post(self, request, *args, **kwargs):
        try:
            params = request.data
            data = {}
            data['username'] = params.get('username')
            data['password'] = params.get('password')
            data['re_password'] = params.get('re_password')
            data['email'] = params.get('email')
            data['first_name'] = params.get('first_name')
            last_name = params.get('last_name')
            
            for key in data:
                if data[key] is None or len(data[key])==0:
                    raise Exception400(key+' cannot be empty')
            
            if data['password'] == data['re_password']:
                if User.objects.filter(username=data['username']).exists():
                    raise Exception400('Username already exists')
                elif User.objects.filter(email=data['email']).exists():
                    raise Exception400('Email already exists')
                else:
                    user = User.objects.create_user(data['username'], password=data['password'], email=data['email'], first_name=data['first_name'], last_name=last_name)
            else:
                raise Exception400('Password do not match')
            
            return Response({'status': 'user created successfully'})
        except Exception as e:
            raise Exception400(e)
        