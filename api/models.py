from django.db import models


# Create your models here.

class RobotCategory(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Robot(models.Model):
    name = models.CharField(max_length=250)
    robot_category = models.ForeignKey(RobotCategory, related_name='robots', on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Commander(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE
    )
    races_count = models.IntegerField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Competition(models.Model):
    commander = models.ForeignKey(
        Commander,
        related_name='competitions',
        on_delete=models.CASCADE
    )
    robot = models.ForeignKey(
        Robot,
        on_delete=models.CASCADE
    )
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # order in descending order
        ordering = ('-distance_in_feet',)
