from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, viewsets
from rest_framework.response import Response

from . import serializers
from .models import Companies, People


class FruitsAndVegetablesViewset(viewsets.ReadOnlyModelViewSet):
    """
    Given a person index (name or guid) returns a list of fruits and vegetables they like.
    """

    queryset = People.objects.all()
    serializer_class = serializers.FruitsVegetablesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("index", "name", "guid")


class CompanyEmployeesViewset(viewsets.ReadOnlyModelViewSet):
    """
    Given a company index (or name) returns all its employees.
    """

    queryset = Companies.objects.all()
    serializer_class = serializers.CompaniesEmployeesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("index", "company")


class TwoPeopleView(views.APIView):
    """
    Given 2 people, provides their information and the list of their
    friends in common who has brown eyes and are still alive.
    """

    def get(self, request, pk1, pk2, format=None):
        people = People.objects.filter(index__in=(pk1, pk2)).filter()
        if people.count() != 2:
            return Response({})
        common_friends = (
            people[0]
            .friends.filter(eyeColor="brown", has_died=False)
            .intersection(people[1].friends.filter(eyeColor="brown", has_died=False))
        )
        twopeople = {
            "person1": people[0],
            "person2": people[1],
            "common_friends": common_friends,
        }
        serializer = serializers.TwoPeopleSerializer(twopeople)
        return Response(serializer.data)
