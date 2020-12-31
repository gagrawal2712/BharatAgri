from rest_framework.views import APIView
from rest_framework.response import Response
from common.exceptions import Exception400
from crop.models import Crop
from django.contrib.auth import authenticate
from django.http import  JsonResponse
from rest_framework.permissions import IsAuthenticated

class ListCrop(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        crops = Crop.objects.all().values()
        crops = list(crops)
        return JsonResponse(crops, safe=False)
        