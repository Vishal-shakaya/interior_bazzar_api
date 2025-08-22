from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.MyMethods import MY_METHODS
from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.Utils.ResponseMessages import RESPONSE_MESSAGES
from app_ib.Utils.ResponseCodes import RESPONSE_CODES
from app_ib.Utils.LocalResponse import LocalResponse
from app_ib.models import LeadQuery, Business
from app_ib.Controllers.Query.Tasks.QueryTasks import LEAD_QUERY_TASK



class LEAD_QUERY_CONTROLLER:

    @classmethod
    async def CreateLeadQuery(self,data):
        try:
            business_ins = None

            is_business_exist = await sync_to_async(Business.objects.filter(pk=data.buss_id).exists)()
            print(f'is_business_exist {is_business_exist}')

            if(is_business_exist):
                 business_ins = await sync_to_async(Business.objects.get)(pk=data.buss_id)
                 print(f'business_ins {business_ins}')   

                 create_query_resp = await  LEAD_QUERY_TASK.CreateLeadQueryTask(business_ins=business_ins,data=data)
                 
                 if create_query_resp:
                    return LocalResponse(
                        response=RESPONSE_MESSAGES.success,
                        message=RESPONSE_MESSAGES.query_assign_success,
                        code=RESPONSE_CODES.success,
                        data=update_resp)

                 else:
                    return LocalResponse(
                        response=RESPONSE_MESSAGES.error,
                        message=RESPONSE_MESSAGES.query_generate_error,
                        code=RESPONSE_CODES.error,
                        data={})

        except Exception as e:
            return LocalResponse(
                response=RESPONSE_MESSAGES.error,
                message=RESPONSE_MESSAGES.query_generate_error,
                code=RESPONSE_CODES.error,
                data={
                    'error': str(e)
                })