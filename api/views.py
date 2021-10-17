# Create your views here.
from rest_framework import generics

from api.models import RobotCategory, Robot, Commander, Competition
from api.serializers import RobotCategorySerializer, RobotSerializer, CommanderSerializer, \
    CommanderCompetitionSerializer


class RobotCategoryList(generics.ListCreateAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer
    name = 'robotcategory-list'


class RobotCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer
    name = 'dronecategory-detail'


class RobotList(generics.ListCreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'drone-list'


class RobotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'drone-list'


class CommanderList(generics.ListCreateAPIView):
    queryset = Commander.objects.all()
    serializer_class = CommanderSerializer
    name = 'commander-list'


class CommanderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commander.objects.all()
    serializer_class = CommanderSerializer
    name = 'pilot-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CommanderCompetitionSerializer
    name = 'competition-list'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CommanderCompetitionSerializer
    name = 'competition-detail'
