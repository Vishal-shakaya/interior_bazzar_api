import httpx
import asyncio
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from adrf.decorators import api_view

# Create your views here.
@api_view(['GET'])
async def TestView(request):
    try:
        # file = request.data.get("lawyer_profile_image")
        # compress_image = await asyncio.gather(helpingMethos.MyImageCompression(type=COMPRESSSION_TYPE.LAWYER_PROFILE, image=file))
        # print(f'compress_image {compress_image[0]}')
        return JsonResponse({"result": ''})
    except Exception as e:
        print(f'{e}')
        return JsonResponse({"fail": ''})


