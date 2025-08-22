from ast import Try
import httpx
import asyncio
from app_ib.Utils.MyMethods import MY_METHODS
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from app_ib.Utils.ServerResponse import ServerResponse
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from app_ib.Controllers.Query.QueryController import LEAD_QUERY_CONTROLLER

@api_view(['POST'])
async def CreateQueryView(request):
    try:
        # Convert request.data to dot notation object
        data = MY_METHODS.json_to_object(request.data)
        
        # Call Auth Controller to Create User
        final_response = await  asyncio.gather(LEAD_QUERY_CONTROLLER.CreateLeadQuery(data=data))
        final_response = final_response[0]

        return ServerResponse(
            response=final_response.response,
            code=final_response.code,
            message=final_response.message,
            data=final_response.data)
        return JsonResponse({'response':"success"})
    except Exception as e:
        # print(f'Error: {e}')
        return ServerResponse(
            response=RESPONSE_MESSAGES.error,
            message=RESPONSE_MESSAGES.query_generate_error,
            code=RESPONSE_CODES.error,
            data={
                'error': str(e)
            })

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