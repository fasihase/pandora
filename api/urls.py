from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register viewsets with it.
router = DefaultRouter()
router.register(
    r"fruits_and_vegetables",
    views.FruitsAndVegetablesViewset,
    basename="fruits_and_vegetables",
)
router.register(r"employees", views.CompanyEmployeesViewset, basename="employees")


# The API URLs are determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "api/twopeople/<int:pk1>/<int:pk2>/",
        views.TwoPeopleView.as_view(),
        name="twopeople",
    ),
]
