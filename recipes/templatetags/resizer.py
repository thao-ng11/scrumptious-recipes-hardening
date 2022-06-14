from django import template

register = template.Library()


@register.filter
def resize_to(ingredient, target):
    servings = ingredient.recipe.servings.all()
    if servings is not None and target is not None:
        try:
            print("SERVE", servings)
            ratio = int(target) / len(servings)
            return ingredient.amount * ratio
        except ValueError:
            pass
    return ingredient.amount


# Get the number of servings from the ingredient's
# recipe using the ingredient.recipe.servings
# properties

# If the servings from the recipe is not None
#   and the value of target is not None
# try
# calculate the ratio of target over
#   servings
# return the ratio multiplied by the
#   ingredient's amount
# catch a possible error
# pass
# return the original ingredient's amount since
#   nothing else worked
