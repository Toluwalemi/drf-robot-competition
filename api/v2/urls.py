from django.urls import path, include

from api.v2.views import ApiRootVersion2
from api.views import RobotCategoryList, RobotCategoryDetail, RobotList, RobotDetail, CommanderList, CommanderDetail, \
    CompetitionList, CompetitionDetail

app_name = 'v2'

urlpatterns = [
    path('vehicle-categories/', RobotCategoryList.as_view(), name=RobotCategoryList.name),
    path('vehicle-categories/<int:pk>/', RobotCategoryDetail.as_view(), name=RobotCategoryDetail.name),
    path('vehicles/', RobotList.as_view(), name=RobotList.name),
    path('vehicles/<int:pk>/', RobotDetail.as_view(), name=RobotDetail.name),
    path('commanders/', CommanderList.as_view(), name=CommanderList.name),
    path('commanders/<int:pk>/', CommanderDetail.as_view(), name=CommanderDetail.name),
    path('competitions/', CompetitionList.as_view(), name=CompetitionList.name),
    path('competitions/<int:pk>/', CompetitionDetail.as_view(), name=CompetitionDetail.name),
    path('', ApiRootVersion2.as_view(), name=ApiRootVersion2.name),
    path('v2/api-auth/', include('rest_framework.urls', namespace='rest_framework.urls')),

]
