from asgiref.sync import sync_to_async
from ast import Try
import time
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.Controllers.Auth.Tasks.AuthTasks import AUTH_TASK
from app_ib.Controllers.Auth.Validators.AuthValidators import AUTH_VALIDATOR
from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.models import UserProfile

class PROFILE_CONTROLLER:
    
    @classmethod 
    async def CreateProfile(self, user_ins , data):

        try:
            print(f'user instance {user_ins}')
            print(f'name {data.name}')
            print(f'email {data.email}')
            print(f'phone {data.phone}')

            is_user_profile_created = await sync_to_async(UserProfile.objects.filter(user=user_ins).exists)()
            print(f'is user profile created {is_user_profile_created}')

            if is_user_profile_created:
                #Create user Profile
                user_profile_ins = await sync_to_async(UserProfile.objects.get)(user=user_ins)
                user_profile_ins.user = user_ins
                user_profile_ins.name = data.name
                user_profile_ins.email = data.email
                user_profile_ins.phone = data.phone
                await sync_to_async(user_profile_ins.save)()
            else:
                user_profile_ins = UserProfile()
                user_profile_ins.user = user_ins
                user_profile_ins.name = data.name
                user_profile_ins.email = data.email
                user_profile_ins.phone = data.phone
                await sync_to_async(user_profile_ins.save)()
            
            return LocalResponse(
                response=RESPONSE_MESSAGES.success,
                message=RESPONSE_MESSAGES.user_profile_create_success,
                code=RESPONSE_CODES.success,
                data={})

        except Exception as e:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_profile_create_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })
            

    @classmethod 
    async def CreateOrUpdateProfileImage(self, user_ins , profile_image):
        try:
            print(f'user instance {user_ins}')
            print(f'profile image {profile_image}')
            
            is_user_profile_created = await sync_to_async(UserProfile.objects.filter(user=user_ins).exists)()
            print(f'is user profile created {is_user_profile_created}')

            # Update Profile Image if already exist : 
            if is_user_profile_created:
                user_profile_ins = await sync_to_async(UserProfile.objects.get)(user=user_ins)
                user_profile_ins.profile_image = profile_image
                await sync_to_async(user_profile_ins.save)()

            # Create Profile Image if not exist : 
            else:
                user_profile_ins = UserProfile()
                user_profile_ins.user = user_ins
                user_profile_ins.profile_image = profile_image
                await sync_to_async(user_profile_ins.save)()
            
            return LocalResponse(
                response=RESPONSE_MESSAGES.success,
                message=RESPONSE_MESSAGES.user_profile_update_success,
                code=RESPONSE_CODES.success,
                data={})

        except Exception as e:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_profile_update_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })

    @classmethod 
    async def GetProfile(self, user_ins):
        try:
            print(f'user instance {user_ins}')
            
            is_user_profile_created = await sync_to_async(UserProfile.objects.filter(user=user_ins).exists)()
            print(f'is user profile created {is_user_profile_created}')
            
            # Update Profile Image if already exist : 
            if is_user_profile_created:
                user_profile_ins = await sync_to_async(UserProfile.objects.get)(user=user_ins)
                user_profile_data = {
                    'name': user_profile_ins.name,
                    'email': user_profile_ins.email,
                    'phone': user_profile_ins.phone,
                    'profile_image': user_profile_ins.profile_image.url,
                }
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_profile_fetch_success,
                    code=RESPONSE_CODES.success,
                    data=user_profile_data)
            

        except Exception as e:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_profile_fetch_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })
