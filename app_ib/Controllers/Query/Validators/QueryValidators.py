from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseMessages import VALIDATION_MESSAGES
from app_ib.Utils import LocalResponse


class QUERY_VALIDATORS:
    @classmethod
    async def _validateQuery(self, data):
        try:
            if not data.name == None or data.name == '':
                return LocalResponse(
                    response=RESPONSE_MESSAGES.error,
                    message=VALIDATION_MESSAGES.query_name_error,
                    code=RESPONSE_CODES.error,
                    data={
                        'error': VALIDATION_MESSAGES.query_name_error
                    })
           
            if not data.phone == None or data.phone == '':
                return LocalResponse(
                    response=RESPONSE_MESSAGES.error,
                    message=VALIDATION_MESSAGES.query_phone_error,
                    code=RESPONSE_CODES.error,
                    data={
                        'error': VALIDATION_MESSAGES.query_phone_error
                    })


            pass; 
        except Exception as e:
            print(f'Error: {e}')
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.query_generate_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })