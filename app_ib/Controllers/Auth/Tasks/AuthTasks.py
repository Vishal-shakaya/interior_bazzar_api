import hashlib
import json
from app_ib.serializers import MyTokenObtainPairSerializer
from app_ib.models import CustomUser, UserProfile
from app_ib.Utils.AppMode import APPMODE_URL
from app_ib.Utils.MyMethods import MY_METHODS
from asgiref.sync import sync_to_async

class AUTH_TASK:

    @classmethod
    async def IsUserExist(self, username):
        try:
            """Check if user exists in database"""
            is_user_exist = await sync_to_async(CustomUser.objects.filter(username=username).exists)()
            return is_user_exist
        except Exception as e:
            print(f'Error in IsUserExist {e}')
            return None

    @classmethod
    async def IsUserExistByMail(self, email):
        try:
            """Check if user exists in database"""
            is_user_exist = await sync_to_async(CustomUser.objects.filter(email=email).exists)()
            return is_user_exist
        except Exception as e:
            print(f'Error in IsUserExist {e}')
            return None
        
    @classmethod
    async def CreateUser(self, username, password, type):
        try:
            """Create user in database"""
            user_ins = CustomUser()
            user_ins.username= username
            user_ins.password= password
            user_ins.type= type
            user_ins.is_active= True
            user_ins.is_delete= False
            await sync_to_async(user_ins.save)()
            return user_ins
        except Exception as e:
            print(f'Error in CreateUser {e}')
            return None

    @classmethod
    async def GenerateUserToken(self, user_ins):
        try:
            """Generate user token"""
            token = await MyTokenObtainPairSerializer.get_token(user=user_ins)
            access_token = token['access']
            refresh_token = token['refresh']
            data = {
                'access_token':access_token,
                'refresh_token':refresh_token,
                'user_type':user_ins.type,
                'user_id':user_ins.id,
                'username':user_ins.username,
                'is_active':user_ins.is_active,
                'is_delete':user_ins.is_delete,
                'unique_id':user_ins.unique_id

            }
            return data
        except Exception as e:
            print(f'Error in GenerateUserToken {e}')
            return None

    @classmethod
    async def LoginUser(self, username, password):
        try:
            """Check if user exists in database"""
            is_user_exist = await sync_to_async(
                CustomUser.objects.filter(username=username, password=password).exists)()
            if is_user_exist:
                user_ins = await sync_to_async(CustomUser.objects.get)(username=username, password=password)
                return user_ins
            return is_user_exist
        except Exception as e:
            print(f'Error in IsUserExist {e}')
            return None

    @classmethod
    async def LogoutUser(self,user_ins):
        try:
            return True
        except Exception as e:
            print(f'Error in IsUserExist {e}')
            return None

    @classmethod
    async def DeleteUser(self,user_ins):
        try:
            user_ins.is_delete= True
            await sync_to_async(user_ins.save)()
            return True
        except Exception as e:
            return None

    @classmethod
    async def GenerateForgotPasswordLink(self,username, timestamp):
        try:
            json_of_hash = {
                'username':username,
                'timestamp':timestamp
            }
            json_of_hash = json.dumps(json_of_hash)
            json_of_hash = hashlib.md5(json_of_hash.encode())
            json_of_hash = json_of_hash.hexdigest()
            link = f'{APPMODE_URL.LOC}v-1/forgot-password/{json_of_hash}'
            return link
        except Exception as e:
            return None

    @classmethod
    async def GetUserProfileInsByUsername(self,username):
        try:
            is_user_exist = await sync_to_async(CustomUser.objects.filter(username=username).exists)()
            if is_user_exist:
                user_ins = await sync_to_async(CustomUser.objects.get)(username=username)
                return user_ins
            else:
                return False
        except Exception as e:
            print(f'Getting user instance error {e}')
            return None

    @classmethod
    async def GetUserProfileByUserInstance(self,user_ins):
        try:
            if user_ins:
                user_profile_ins = await sync_to_async(UserProfile.objects.filter(user=user_ins).first)()
                print(f'user_profile_ins {user_profile_ins}')
                return user_profile_ins
            else:
                return False
        except Exception as e:
            print(f'Getting user profile instance error {e}')
            return None


    @classmethod
    async def ResetPassword(self, user_ins, data):
        try:
            """Reset user password"""
            print(f'db old passwod {user_ins.password} , old passwod{data.old_password}')
            if(user_ins.password==data.old_password):
                user_ins.password = data.password
                await sync_to_async(user_ins.save)()
                print(f'updated password {user_ins.password}')
                return True
            else:
                return False
        except Exception as e:
            print(f'Error in ResetPassword {e}')
            return None
