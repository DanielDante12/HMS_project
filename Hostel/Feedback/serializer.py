from rest_framework.serializers import ModelSerializer
from .models import Hostel, Feedback, Room

class HostelSerializer(ModelSerializer):
    class Meta:
        model= Hostel
        fields='__all__'

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'    

class RoomSerializer(ModelSerializer):
    class Meta:
        model =  Room
        fields = '__all__'               
