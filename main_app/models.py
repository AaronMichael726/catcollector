from django.db import models

# Create your models here.
class Cat(models.Model):
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# tuples (value1, value2, value3) immutable pop() no changing of the values
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
    date = models.DateField('When are we getting fed')
    meal = models.CharField(
        max_length = 1, 
        choices = MEALS, 
        default = MEALS[0][0]
    )

    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
