from ast import Try
import httpx
import asyncio
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from types import SimpleNamespace
from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.Controllers.Auth.AuthController import AUTH_CONTROLLER
from app_ib.Utils.ServerResponse import ServerResponse
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES


@api_view(['POST'])
async def SignupView(request):
    try:
        # Convert request.data to dot notation object
        data = MY_METHODS.json_to_object(request.data)
        
        # Test
        # print(f'user {data.username}')
        # print(f'password {data.password}')
        # print(f'type {data.type}')
        
        # Call Auth Controller to Create User
        auth_resp = await  asyncio.gather(AUTH_CONTROLLER.SignupUser(data=data))
        auth_resp = auth_resp[0]
        # print(f'auth_resp {auth_resp.data}')

        return ServerResponse(
            response=RESPONSE_MESSAGES.success,
            message=RESPONSE_MESSAGES.user_register_success,
            code=RESPONSE_CODES.success,
            data=auth_resp.data)

    except Exception as e:
        print(f'Error: {e}')
        return ServerResponse(
            response=RESPONSE_MESSAGES.error,
            message=RESPONSE_MESSAGES.user_register_error,
            code=RESPONSE_CODES.error,
            data={
                'error': str(e)
            })



@api_view(['POST'])
async def LoginView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'Error: {e}')
        return JsonResponse({"result": 'error'})


async def LogoutView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def ForgotPasswordRequestView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def ForgotPasswordView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})
        
async def PasswordResetView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})

async def DeleteAccountView(request):
    try:
        return JsonResponse({"result": 'success'})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"result": 'error'})





