from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Companies, People


class ModelTest(TestCase):
    """This class defines the test suite for models."""

    def setUp(self):
        """Define the test client and other test variables."""

    def tearDown(self):
        """Destroy resources and remove temporaries after test."""

    def test_create_people(self):
        """Test the People model by creating a person."""
        person = People(index=0)
        prvCount = People.objects.count()
        person.save()
        currCount = People.objects.count()
        self.assertNotEqual(prvCount, currCount)

    def test_create_companies(self):
        """Test the Companies model by creating a company."""
        company = Companies(index=0)
        prvCount = Companies.objects.count()
        company.save()
        currCount = Companies.objects.count()
        self.assertNotEqual(prvCount, currCount)


class ViewTest(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.person1 = {
            "name": "Amy Goff",
            "index": 1,
        }
        self.person2 = {
            "name": "Kim York",
            "index": 2,
        }
        company = Companies(index=1)
        company.save()
        People(company=company, **self.person1).save()
        People(company=company, **self.person2).save()
        self.client = APIClient()

    def test_twopeople(self):
        """API returns response with two people."""
        response = self.client.get(
            reverse(
                "twopeople",
                kwargs={"pk1": self.person1["index"], "pk2": self.person2["index"]},
            ),
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.person1["name"])
        self.assertContains(response, self.person2["name"])

    def test_get_employees(self):
        """API returns response for company with Employees."""
        response = self.client.get(
            reverse("employees-detail", kwargs={"pk": self.person1["index"]}),
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.person1["name"])
        self.assertContains(response, self.person2["name"])

    def test_get_no_employees(self):
        """API returns response for invalid company index provided."""
        response = self.client.get(reverse("employees-detail", kwargs={"pk": 9999}), format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_fruits_and_vegetables(self):
        """API returns response for employees with their favurite fruits and vegitables."""
        response = self.client.get(
            reverse("fruits_and_vegetables-detail", kwargs={"pk": self.person1["index"]}),
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.person1["name"])

    def test_get_no_fruits_and_vegetables(self):
        """API returns response for invalid index provided."""
        response = self.client.get(
            reverse("fruits_and_vegetables-detail", kwargs={"pk": 9999}), format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
