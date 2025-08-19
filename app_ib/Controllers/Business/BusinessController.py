from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.models import Business, CustomUser
from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.Utils.LocalResponse import LocalResponse


class BUSS_CONTROLLER:
    @classmethod
    async def CreateBusiness(self, user_ins, data):
        try:
            print(f'business user {user_ins}')
            print(f'business data {data.business_name}')
            print(f'business data {data.phone}')
            print(f'business data {data.gst}')
            print(f'business data {data.since}')
            print(f'business data {data.segment}')
            print(f'business data {data.catigory}')   
            
            return LocalResponse(
                code=RESPONSE_CODES.success,
                response=RESPONSE_MESSAGES.success,
                message=RESPONSE_MESSAGES.business_register_success,
                data={})
        except Exception as e:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.business_register_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })