import asyncio
from profile import Profile
from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from app_ib.Utils.ServerResponse import ServerResponse
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.models import Business, UserProfile
from app_ib.Controllers.BusinessProfile.Tasks.BusinessProfileTasks import BUSS_PROF_TASK

@api_view(['GET'])
async def GetBusinessByPaginationView(request,index):
    try:
        print(f'page index {index}')

        user_profile_data=None
        async for business in Business.objects.all():
            print(f'business {business}')
            print(f'user {business.user}')
            user_ins = business.user
            
            is_profile_ins_exist= await sync_to_async(UserProfile.objects.filter(user=user_ins).exists)()
            print(f'is_profile_ins_exist  {is_profile_ins_exist}')

            if(is_profile_ins_exist):
                profile_ins= await sync_to_async(UserProfile.objects.get)(user=user_ins)
                


        return JsonResponse({'response':"success"})

        # return ServerResponse(
        #     response=auth_resp.response,
        #     code=auth_resp.code,
        #     message=auth_resp.message,
        #     data=auth_resp.data)
    except Exception as e:
        return ServerResponse(
            response=RESPONSE_MESSAGES.error,
            message=RESPONSE_MESSAGES.default_error,
            code=RESPONSE_CODES.error,
            data={
                'error': str(e)
            })

