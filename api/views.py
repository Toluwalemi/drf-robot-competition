# Create your views here.
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle

from api.helpers import custompermission
from api.helpers.custom_competition_filter import CompetitionFilter
from api.models import RobotCategory, Robot, Commander, Competition
from api.serializers import RobotCategorySerializer, RobotSerializer, CommanderSerializer, \
    CommanderCompetitionSerializer


class RobotCategoryList(generics.ListCreateAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer
    name = 'robotcategory-list'
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class RobotCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer
    name = 'robotcategory-detail'


class RobotList(generics.ListCreateAPIView):
    throttle_scope = 'robots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'robot-list'
    filter_fields = ('name', 'robot_category', 'manufacturing_date', 'has_it_competed',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'manufacturing_date',)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RobotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'robots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'robot-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )


class CommanderList(generics.ListCreateAPIView):
    throttle_scope = 'commanders'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Commander.objects.all()
    serializer_class = CommanderSerializer
    name = 'commander-list'
    filter_fields = ('name', 'gender', 'races_count',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'races_count',)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CommanderDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'commanders'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Commander.objects.all()
    serializer_class = CommanderSerializer
    name = 'commander-detail'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CommanderCompetitionSerializer
    name = 'competition-list'
    filter_class = CompetitionFilter
    ordering_fields = ('distance_in_feet', 'distance_achievement_date',)


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
