from django.contrib import admin

from .models import Companies, People


class PeopleAdmin(admin.ModelAdmin):
    search_fields = (
        "index",
        "name",
    )


class CompaniesAdmin(admin.ModelAdmin):
    list_display = ["index", "company"]


admin.site.register(People, PeopleAdmin)
admin.site.register(Companies, CompaniesAdmin)
