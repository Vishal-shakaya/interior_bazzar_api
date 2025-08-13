from ast import Try

from adrf.views import sync_to_async
from app_ib.models import CustomUser
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from interior_bazzar.backend.interior_bazzar.app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse



class AUTH_CONTROLLER: 
    async def SignupUser(self, data):
        try:
            # Check if user already exist 
            # if not then create else send message that user already exist
            is_user_exist = await sync_to_async(CustomUser.objects.filter(username=data.username).exists)() 
            print(f'is user exist {is_user_exist}')

            if is_user_exist:
                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_exist,
                    code=RESPONSE_CODES.success,
                    data={})
            else:
                #Create User with username and password
                user_ins = await sync_to_async(CustomUser.objects.get)(username=data.username)
                print(f'get user instance {user_ins}')
                # Save User
                user_ins.username= data.username
                user_ins.password= data.password
                user_ins.type= data.type
                user_ins.is_active= True
                user_ins.is_delete= False
                await sync_to_async(user_ins.save)()
            
                # Generate Auth Token: 
                token = await sync_to_async(MyTokenObtainPairSerializer.get_token)(user_ins)
                access_token = token['access']
                refresh_token = token['refresh']
                print(f'access_token {access_token}')
                print(f'refresh_token {refresh_token}')

                # Create Object with tokens and user type
                response_data = {
                    'access_token':access_token,
                    'refresh_token':refresh_token,
                    'user_type':user_ins.type
                }
                print(f'response_data {response_data}')


                return LocalResponse(
                    response=RESPONSE_MESSAGES.success,
                    message=RESPONSE_MESSAGES.user_register_success,
                    code=RESPONSE_CODES.success,
                    data=response_data)


        except:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.user_register_error,
                code=RESPONSE_CODES.error,
                data={})

