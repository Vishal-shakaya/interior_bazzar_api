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
from app_ib.Controllers.Auth.Validators.AuthValidators import AUTH_VALIDATOR
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
async def SignupView(request):
    try:
        # Convert request.data to dot notation object
        data = MY_METHODS.json_to_object(request.data)

        # Call Auth Controller to Create User
        auth_resp = await  asyncio.gather(AUTH_CONTROLLER.SignupUser(data=data))
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
            message=RESPONSE_MESSAGES.user_register_error,
            code=RESPONSE_CODES.error,
            data={
                'error': str(e)
            })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
async def PasswordResetView(request):
    try:
        # Convert request.data to dot notation object
        data = MY_METHODS.json_to_object(request.data)
        user_ins = request.user
        
        # Call Auth Controller to Create User
        auth_resp = await  asyncio.gather(AUTH_CONTROLLER.ResetPassword(user_ins=user_ins, data=data))
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





