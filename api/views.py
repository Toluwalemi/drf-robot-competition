# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

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
    name = 'robotcategory-detail'


class RobotList(generics.ListCreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'robot-list'


class RobotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'robot-detail'


class CommanderList(generics.ListCreateAPIView):
    queryset = Commander.objects.all()
    serializer_class = CommanderSerializer
    name = 'commander-list'


class CommanderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commander.objects.all()
    serializer_class = CommanderSerializer
    name = 'commander-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CommanderCompetitionSerializer
    name = 'competition-list'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CommanderCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'robot-categories': reverse(RobotCategoryList.name, request=request),
            'robots': reverse(RobotList.name, request=request),
            'commanders': reverse(CommanderList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
        })
