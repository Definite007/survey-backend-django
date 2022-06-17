from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from home.serializers import FeedSerializer
from rest_framework.parsers import JSONParser
from home.models import Feedback
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    if request.method=='POST':
        feed_data=JSONParser().parse(request)
        feed_serializer = FeedSerializer(data=feed_data)
        if feed_serializer.is_valid():
            feed_serializer.save()
        return JsonResponse("Added Successfully!!" , safe=False)
    feedback = Feedback.objects.all()
    feed_serializer = FeedSerializer(feedback, many=True)
    context = {"data": feed_serializer.data}
    return render(request,'index.html', context)
        # feed_serializer.data, safe=False


    # https://git.heroku.com/survey-backend-kiosk.git | https://survey-backend-kiosk.herokuapp.com/
