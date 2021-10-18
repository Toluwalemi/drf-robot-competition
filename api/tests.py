from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from api.models import RobotCategory
from api.views import RobotCategoryList


class RobotCategoryTests(APITestCase):
    def post_robot_category(self, name):
        url = reverse(RobotCategoryList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_robot_category(self):
        """
        Test to create a new RobotCategory and retrieve it
        """
        new_robot_category_name = 'Humanoid'
        response = self.post_robot_category(new_robot_category_name)
        print("PK {0}".format(RobotCategory.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert RobotCategory.objects.count() == 1
        assert RobotCategory.objects.get().name == new_robot_category_name

    def test_post_existing_robot_category_name(self):
        """
        Test to avoid duplicate robot category
        """
        url = reverse(RobotCategoryList.name)
        new_robot_category_name = 'Duplicated Copter'
        data = {'name': new_robot_category_name}
        response1 = self.post_robot_category(new_robot_category_name)
        assert response1.status_code == status.HTTP_201_CREATED
        response2 = self.post_robot_category(new_robot_category_name)
        print(response2)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
