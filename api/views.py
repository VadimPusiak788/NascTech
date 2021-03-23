from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import *


class TestExample(APIView):

    parser_classes = [JSONParser]

    def get(self, request):
        rule = request.data['rule']
        data = request.data['data']

        for i in rule:
            data = list(map(eval('fun_'+i), data))

        return Response({'result': data}, status=200)