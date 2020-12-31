from rest_framework.views import APIView
from rest_framework.response import Response
from common.exceptions import Exception400
from crop.models import Crop
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class AddCrop(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        crops = request.data
        crop_data = []
        for crop in crops:
            crop_data.append(
                Crop(
                    name=crop,
                    feature1=crops[crop].get('feature1'),
                    feature2=crops[crop].get('feature2'),
                    feature3=crops[crop].get('feature3'),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            )
        Crop.objects.bulk_create(crop_data)
        return Response('crop added successfully')