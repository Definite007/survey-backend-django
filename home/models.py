from django.db import models

# Create your models here.
class Feedback(models.Model):
    rating1 = models.IntegerField(null=True)
    rating2 = models.IntegerField(null=True)
    rating3 = models.IntegerField(null=True)
    rating4 = models.IntegerField(null=True)
    feedback = models.TextField(null=True)


    def __str__(self):
        return self.feedback
