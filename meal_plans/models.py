from django.db import models

from recipes.models import USER_MODEL


# Create your models here.
class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField()
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="meal_plans",
        on_delete=models.CASCADE,
    )
    recipes = models.ManyToManyField(
        "recipes.Recipe", related_name="meal_plans"
    )

    def __str__(self):
        return f"{self.name}"
