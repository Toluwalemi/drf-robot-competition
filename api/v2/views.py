from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.views import RobotCategoryList, RobotList, CommanderList, CompetitionList


class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'vehicle-categories': reverse(RobotCategoryList.name, request=request),
            'vehicles': reverse(RobotList.name, request=request),
            'commanders': reverse(CommanderList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
        })
