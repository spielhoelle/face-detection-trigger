from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import json


@csrf_exempt
@parser_classes((JSONParser,))
def index(request):
    json_body = json.loads(request.body)
    # TODO do something
    print(json_body["side"])
    return JsonResponse({"res": json_body["side"]})
