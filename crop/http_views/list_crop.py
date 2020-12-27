from rest_framework.views import APIView
from rest_framework.response import Response
from common.exceptions import Exception400
from crop.models import Crop
from django.contrib.auth import authenticate
from django.http import  JsonResponse

class ListCrop(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            crops = Crop.objects.all().values()
            crops = list(crops)
            return JsonResponse(crops, safe=False)
        else:
            raise Exception400('login required')
        