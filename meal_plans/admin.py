from django.contrib import admin
from meal_plans.models import MealPlan

# Register your models here.
class MealPlansAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlansAdmin)
