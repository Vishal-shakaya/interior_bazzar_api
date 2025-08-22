from asgiref.sync import sync_to_async
from app_ib.models import LeadQuery

class LEAD_QUERY_TASK:

    @classmethod
    async def CreateLeadQueryTask(self, business_ins, data):
        try:
            lead_query_ins = LeadQuery()
            lead_query_ins.business= business_ins
            await sync_to_async(lead_query_ins.save)()
            return True
            
        except Exception as e:
            print(f'Error in CreateLeadQueryTask {e}')
            return None
