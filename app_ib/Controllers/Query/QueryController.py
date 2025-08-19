from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.Controllers.Query.Validators.QueryValidators import QUERY_VALIDATORS
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse

class QUERY_CONTROLLER: 
    @classmethod
    async def CrateQuery(self, user_ins, buss_ins, data):
        try:
            ######################################
            # 1.validate Lead query parameters
            ######################################

            # query_resp = await QUERY_VALIDATORS.ValidateQuery(data)
            # if query_resp.response != RESPONSE_MESSAGES.success:
            #     return query_resp

            ######################################
            # 2. create Lead query
            ######################################
            print(f'user_ins {user_ins}')
            print(f'buss_ins {buss_ins}')
            print(f'name {data.name}')
            print(f'email {data.email}')
            print(f'phone {data.phone}')
            print(f'interested {data.interested}')
            print(f'query {data.query}')
            print(f'city {data.city}')
            print(f'city {data.country}')
            
            return LocalResponse(
                response=RESPONSE_MESSAGES.success,
                message=RESPONSE_MESSAGES.query_generate_success,
                code=RESPONSE_CODES.success,
                data={})

        except Exception as e:
            print(f'Error: {e}')
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.query_generate_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })
