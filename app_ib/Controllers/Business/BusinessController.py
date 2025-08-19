from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from app_ib.models import Business, CustomUser
from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse


class BUSS_CONTROLLER:

    @classmethod
    async def CreateBusinessController(self, user_ins, data):
        try:
            # print(f'business user {user_ins}')
            # print(f'business data {data.business_name}')
            # print(f'business data {data.phone}')
            # print(f'business data {data.gst}')
            # print(f'business data {data.since}')
            # print(f'business data {data.segment}')
            # print(f'business data {data.catigory}')   
            
            # Valiate Business data
            validate_business_name= await BUSS_VALIDATOR._validate_business_name(business_name=data.business_name)
            if validate_business_name.code == RESPONSE_CODES.error:
                return LocalResponse(
                    code=validate_business_name.code,
                    response=validate_business_name.response,
                    message=validate_business_name.message,
                    data={})

            validate_business_phone= await BUSS_VALIDATOR._validate_business_phone(phone=data.phone)
            validate_business_gst= await BUSS_VALIDATOR._validate_business_gst(gst=data.gst)
            validate_business_since= await BUSS_VALIDATOR._validate_business_since(since=data.since)
            validate_business_segment= await BUSS_VALIDATOR._validate_business_segment(segment=data.segment)
            validate_business_catigory= await BUSS_VALIDATOR._validate_business_catigory(catigory=data.catigory)




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