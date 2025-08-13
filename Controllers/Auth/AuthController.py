from ast import Try

from adrf.views import sync_to_async
from app_ib.models import CustomUser
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.serializers import MyTokenObtainPairSerializer



class AUTH_CONTROLLER:
    
    @classmethod 
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
                user_ins = CustomUser()
                print(f'user instance {user_ins}')
                print(f' username {data.username}')
                print(f' password {data.password}')
                print(f' type {data.type}')



                # Save User
                user_ins.username= data.username
                user_ins.password= data.password
                user_ins.type= data.type
                user_ins.is_active= True
                user_ins.is_delete= False

                await sync_to_async(user_ins.save)()

                print(f'user created {user_ins.username}')

                # Generate Auth Token: 
                try:
                    token = await MyTokenObtainPairSerializer.get_token(user=user_ins)
                    access_token = token['access']
                    refresh_token = token['refresh']
                    print(f'access_token {access_token}')
                    print(f'refresh_token {refresh_token}')
                except BaseException as e:
                    print(f'error {e} ')

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

