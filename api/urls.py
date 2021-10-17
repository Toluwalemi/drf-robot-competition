from django.urls import path

from .views import RobotCategoryList, RobotCategoryDetail, RobotList, RobotDetail, CommanderList, CommanderDetail, \
    CompetitionList, CompetitionDetail, ApiRoot

urlpatterns = [
    path('robot-categories/', RobotCategoryList.as_view(), name=RobotCategoryList.name),
    path('robot-categories/<int:pk>/', RobotCategoryDetail.as_view(), name=RobotCategoryDetail.name),
    path('robots/', RobotList.as_view(), name=RobotList.as_view()),
    path('robots/<int:pk>)/', RobotDetail.as_view(), name=RobotDetail.as_view()),
    path('commanders/', CommanderList.as_view(), name=CommanderList.as_view()),
    path('commanders/<int:pk>)/', CommanderDetail.as_view(), name=CommanderDetail.as_view()),
    path('competitions/', CompetitionList.as_view(), name=CompetitionList.as_view()),
    path('competitions/<int:pk>)/', CompetitionDetail.as_view(), name=CompetitionDetail.as_view()),
    path('', ApiRoot.as_view(), name=ApiRoot.as_view()),

]
