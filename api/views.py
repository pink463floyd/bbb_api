from django.shortcuts import render
from django.http import HttpResponse
from api.models import Stops
from api.serializers import StopsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#@csrf_exempt
def stops_list(request):
    print("meter list");
    if request.method == 'GET':
        stops = Stops.objects.all()
        serializer = StopsSerializer(stops, many=True)
        return JSONResponse(serializer.data)

#@csrf_exempt
def stops_detail(request, pk):
    print("meter detail" + pk);
    stop = Stops.objects.get(stop_id__exact=pk)
    serializer = StopsSerializer(stop)
    return JSONResponse(serializer.data)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

