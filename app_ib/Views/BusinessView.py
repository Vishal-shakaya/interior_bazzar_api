from ast import Try
import httpx
import asyncio
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.Controllers.Business.BusinessController import BUSS_CONTROLLER
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from app_ib.Utils.ServerResponse import ServerResponse
from app_ib.Utils.ResponseCodes import RESPONSE_CODES


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
async def CreateBusinessView(request):
    try:
        # Convert request.data to dot notation object
        data = MY_METHODS.json_to_object(request.data)
        user_ins = request.user

        # Call Auth Controller to Create User
        auth_resp = await  asyncio.gather(BUSS_CONTROLLER.CreateBusiness(user_ins=user_ins, data=data))
        print(f'auth_resp {auth_resp}')
        auth_resp = auth_resp[0]

        return ServerResponse(
            response=auth_resp.response,
            code=auth_resp.code,
            message=auth_resp.message,
            data=auth_resp.data)

    except Exception as e:
        # print(f'Error: {e}')
        return ServerResponse(
            response=RESPONSE_MESSAGES.error,
            message=RESPONSE_MESSAGES.business_register_error,
            code=RESPONSE_CODES.error,
            data={
                'error': str(e)
            })


async def UpdateBusinessView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def GetBusinessByIdView(request,id):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def GetAllBusinessView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})