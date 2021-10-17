from rest_framework import serializers

from api.models import RobotCategory, Robot, Competition, Commander


class RobotCategorySerializer(serializers.HyperlinkedModelSerializer):
    robot = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='drone-detail'
    )

    class Meta:
        model = RobotCategory
        fields = ('url', 'pk', 'name', 'robots')


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    # display the category name
    robot_category = serializers.SlugRelatedField(queryset=RobotCategory.objects.all(),
                                                  slug_field='name')

    class Meta:
        model = Robot
        fields = ('url', 'name', 'robot_category',
                  'manufacturing_date', 'has_it_completed', 'created')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    # display all the details for the related robot
    robot = RobotSerializer()

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'distance_in_feet',
                  'distance_achievement_date', 'robot')


class CommanderSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Commander.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model = Commander
        fields = ('url', 'name', 'gender', 'gender_description',
                  'races_count', 'created', 'competitions')


class CommanderCompetitionSerializer(serializers.ModelSerializer):
    # display the commander's name
    commander = serializers.SlugRelatedField(queryset=Commander.objects.all(),
                                             slug_field='name')
    # display the robot's name
    robot = serializers.SlugRelatedField(queryset=Robot.objects.all(),
                                         slug_field='name')

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date',
                  'commander', 'robot')
