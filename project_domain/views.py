# from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import project_domain_view
from rest_framework.response import Response
from project_domain.models import YourModel
from project_domain.serializers import YourModelSerializer

@project_domain_view(['GET'])
def get_table(request):
    table = YourModel.scan()
    serializer = YourModelSerializer(stores, many=True)
    return Response(serializer.data)
