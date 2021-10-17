import django_filters
from django_filters import DateTimeFilter, NumberFilter, AllValuesFilter

from api.models import Competition


class CompetitionFilter(django_filters.FilterSet):
    from_achievement_date = DateTimeFilter(
        field_name='distance_achievement_date', lookup_expr='gte'
    )
    to_achievement_date = DateTimeFilter(
        field_name='distance_achievement_date', lookup_expr='lte'
    )
    min_distance_in_feet = NumberFilter(
        field_name='distance_in_feet', lookup_expr='gte'
    )
    max_distance_in_feet = NumberFilter(
        field_name='distance_in_feet', lookup_expr='lte'
    )
    robot_name = AllValuesFilter(field_name='robot__name')
    commander_name = AllValuesFilter(field_name='commander__name')

    class Meta:
        model = Competition
        fields = (
            'distance_in_feet', 'from_achievement_date',
            'to_achievement_date', 'min_distance_in_feet',
            'max_distance_in_feet',
        )
        # robot_name will be accessed as robot_name
        # commander__name will be accessed as commander_name
