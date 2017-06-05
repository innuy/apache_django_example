# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from models import Example


# Create your views here.

class IndexView(APIView):

    def get(self, request):
        examples = Example.objects.all()
        result = []
        for example in examples:
            data = {
                'id': example.example_id,
                'name': example.name
            }
            result.append(data)
        return JsonResponse(result, safe=False)


