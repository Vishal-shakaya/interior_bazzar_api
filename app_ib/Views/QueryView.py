from ast import Try
import httpx
import asyncio
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from adrf.decorators import api_view

async def CreateQueryView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def GetQueryByIdView(request,id):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def GetQueryBusinessIdView(request,id):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})