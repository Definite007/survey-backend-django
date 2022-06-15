from django.http import JsonResponse
from home.serializers import FeedSerializer
from rest_framework.parsers import JSONParser
from home.models import Feedback

# Create your views here.
def index(request):
    if request.method=='POST':
        feed_data=JSONParser().parse(request)
        feed_serializer = FeedSerializer(data=feed_data)
        if feed_serializer.is_valid():
            feed_serializer.save()
        return JsonResponse("Added Successfully!!" , safe=False)
    return JsonResponse("Failed to Add.",safe=False)


    # https://survey-backend-kiosk.herokuapp.com/ | https://git.heroku.com/survey-backend-kiosk.git