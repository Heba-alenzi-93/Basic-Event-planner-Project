from django.contrib import admin
from .models import EvenPlanner



class PlannerAdmin(admin.ModelAdmin):
    list_display =  ("organizer","name")
    list_filter = ("name",)
# Register your models here.
admin.site.register(EvenPlanner,PlannerAdmin)