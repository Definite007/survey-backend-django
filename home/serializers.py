from dataclasses import fields
from rest_framework import serializers
from home.models import Feedback

class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = (
            'rating1',
            'rating2',
            'rating3',
            'rating4',
            'feedback'
        )