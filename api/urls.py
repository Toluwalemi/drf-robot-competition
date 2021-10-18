from django.urls import path

from .views import RobotCategoryList, RobotCategoryDetail, RobotList, RobotDetail, CommanderList, CommanderDetail, \
    CompetitionList, CompetitionDetail, ApiRoot

app_name = 'v1'

urlpatterns = [
    path('robot-categories/', RobotCategoryList.as_view(), name=RobotCategoryList.name),
    path('robot-categories/<int:pk>/', RobotCategoryDetail.as_view(), name=RobotCategoryDetail.name),
    path('robots/', RobotList.as_view(), name=RobotList.name),
    path('robots/<int:pk>/', RobotDetail.as_view(), name=RobotDetail.name),
    path('commanders/', CommanderList.as_view(), name=CommanderList.name),
    path('commanders/<int:pk>/', CommanderDetail.as_view(), name=CommanderDetail.name),
    path('competitions/', CompetitionList.as_view(), name=CompetitionList.name),
    path('competitions/<int:pk>/', CompetitionDetail.as_view(), name=CompetitionDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),

]
